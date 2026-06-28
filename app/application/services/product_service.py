from app.application.dtos.product_dto import CreateProductInput
from app.application.repositories.product_repository import ProductRepository
from app.domain.entities.product import Product
from app.domain.excpetions.exception import InvalidValueError


class ProductService:
    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def create_product(self, data: CreateProductInput) -> Product:
        if data.sale_price < 0 or data.cost_price < 0:
            raise InvalidValueError("Preços não podem ser negativos.")

        product = Product(
            id=None,
            name=data.name,
            category=data.category,
            sale_price=data.sale_price,
            cost_price=data.cost_price,
            active=data.active,
        )
        return self._repository.create(product)

    def list_products(self) -> list[Product]:
        return self._repository.list_all()