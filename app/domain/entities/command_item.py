from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from app.domain.enums import ProductCategory


@dataclass
class CommandItem:
    id: Optional[int]
    command_id: Optional[int]
    product_id: int
    product_name: str
    category: ProductCategory
    quantity: int
    unit_price: Decimal
    subtotal: Decimal

