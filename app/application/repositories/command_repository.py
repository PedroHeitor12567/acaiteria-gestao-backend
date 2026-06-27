from abc import ABC, abstractmethod
from typing import Optional

from datetime import datetime

from app.domain.entities.command import Command
from app.domain.entities.command_item import CommandItem


class CommandRepository(ABC):
    @abstractmethod
    def create(self, command: Command) -> Command: ...

    @abstractmethod
    def get_by_id(self, command_id: int) -> Optional[Command]: ...

    @abstractmethod
    def update(self, command: Command) -> Command: ...

    @abstractmethod
    def list_all(self) -> list[Command]: ...

    @abstractmethod
    def add_item(self, command_id: int, item: CommandItem) -> CommandItem: ...

    @abstractmethod
    def get_item(self, command_id: int, item_id: int) -> Optional[CommandItem]: ...

    @abstractmethod
    def remove_item(self, command_id: int, item_id: int) -> None: ...

    @abstractmethod
    def next_command_number(self) -> int: ...

    @abstractmethod
    def list_closed_between(self, start: datetime, end: datetime) -> list[Command]: ...