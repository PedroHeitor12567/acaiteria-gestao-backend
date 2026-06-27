from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

from app.domain.enums import ProductCategory


@dataclass
class Product:
    id: Optional[int]
    name: str
    category: ProductCategory
    sale_price: Decimal
    cost_price: Decimal
    active: bool = True