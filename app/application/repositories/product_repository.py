from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product: ...

    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]: ...

    @abstractmethod
    def list_all(self) -> list[Product]: ...
