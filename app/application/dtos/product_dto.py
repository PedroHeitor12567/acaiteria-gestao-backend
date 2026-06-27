from dataclasses import dataclass
from decimal import Decimal

from app.domain.enums.product_catetgory import ProductCategory


@dataclass
class CreateProductInput:
    name: str
    category: ProductCategory
    sale_price: Decimal
    cost_price: Decimal
    active: bool = True
