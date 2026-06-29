from datetime import datetime
from decimal import Decimal

from app.application.dtos.command_dto import AddCommandItemInput
from app.application.repositories.command_repository import CommandRepository
from app.application.repositories.product_repository import ProductRepository
from app.domain.entities.command import Command, CommandItem
from app.domain.enums.command_status import CommandStatus
from app.domain.excpetions.exception import InvalidQuantityError, CommandNotFoundError, CommandNotOpenError, \
    ProductNotFoundError, InactiveProductError, CommandItemNotFoundError, EmptyCommandError


class CommandService:
    def __init__(self, command_repository: CommandRepository, product_repository: ProductRepository):
        self._command_repository = command_repository
        self._product_repository = product_repository

    def open_command(self) -> Command:
        command = Command(
            id=None,
            command_number=self._command_repository.next_command_number(),
            opened_at=datetime.utcnow(),
            closed_at=None,
            status=CommandStatus.OPEN,
            total=Decimal("0.00"),
        )
        return self._command_repository.create(command)

    def add_item(self, command_id: int, data: AddCommandItemInput) -> CommandItem:
        if data.quantity < 1:
            raise InvalidQuantityError("A quantidade deve ser maior ou igual a 1.")

        command = self._command_repository.get_by_id(command_id)
        if command is None:
            raise CommandNotFoundError(f"Comanda {command_id} não encontrada.")
        if command.status != CommandStatus.OPEN:
            raise CommandNotOpenError("Não é possível adicionar itens a uma comanda que não está OPEN.")

        product = self._product_repository.get_by_id(data.product_id)
        if product is None:
            raise ProductNotFoundError(f"Produto {data.product_id} não encontrado.")
        if not product.active:
            raise InactiveProductError("Não é possível adicionar um produto inativo.")

        unit_price = product.sale_price
        subtotal = unit_price * data.quantity

        item = CommandItem(
            id=None,
            command_id=command_id,
            product_id=product.id,
            product_name=product.name,
            category=product.category,
            quantity=data.quantity,
            unit_price=unit_price,
            subtotal=subtotal,
        )
        created_item = self._command_repository.add_item(command_id, item)
        self._recalculate_total(command_id)
        return created_item

    def remove_item(self, command_id: int, item_id: int) -> None:
        command = self._command_repository.get_by_id(command_id)
        if command is None:
            raise CommandNotFoundError(f"Comanda {command_id} não encontrada.")
        if command.status != CommandStatus.OPEN:
            raise CommandNotOpenError("Não é possível remover itens de uma comanda que não está OPEN.")

        item = self._command_repository.get_item(command_id, item_id)
        if item is None:
            raise CommandItemNotFoundError(f"Item {item_id} não encontrado na comanda {command_id}.")

        self._command_repository.remove_item(command_id, item_id)
        self._recalculate_total(command_id)

    def close_command(self, command_id: int) -> Command:
        command = self._command_repository.get_by_id(command_id)
        if command is None:
            raise CommandNotFoundError(f"Comanda {command_id} não encontrada.")
        if command.status != CommandStatus.OPEN:
            raise CommandNotOpenError("Apenas comandas OPEN podem ser fechadas.")
        if len(command.items) == 0:
            raise EmptyCommandError("Não é possível fechar uma comanda vazia.")

        command.status = CommandStatus.CLOSED
        command.closed_at = datetime.now()
        command.total = sum((item.subtotal for item in command.items), Decimal("0.00"))
        return self._command_repository.update(command)

    def cancel_command(self, command_id: int) -> Command:
        command = self._command_repository.get_by_id(command_id)
        if command is None:
            raise CommandNotFoundError(f"Comanda {command_id} não encontrada.")
        if command.status != CommandStatus.OPEN:
            raise CommandNotOpenError("Apenas comandas OPEN podem ser canceladas.")

        command.status = CommandStatus.CANCELED
        command.closed_at = datetime.now()
        return self._command_repository.update(command)

    def get_command(self, command_id: int) -> Command:
        command = self._command_repository.get_by_id(command_id)
        if command is None:
            raise CommandNotFoundError(f"Comanda {command_id} não encontrada.")
        return command

    def list_commands(self) -> list[Command]:
        return self._command_repository.list_all()

    def _recalculate_total(self, command_id: int) -> None:
        command = self._command_repository.get_by_id(command_id)
        command.total = sum((item.subtotal for item in command.items), Decimal("0.00"))
        self._command_repository.update(command)