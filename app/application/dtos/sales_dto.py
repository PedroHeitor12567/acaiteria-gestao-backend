from dataclasses import dataclass
from decimal import Decimal

from app.domain.enums.product_catetgory import ProductCategory


@dataclass
class CategorySalesOutput:
    category: ProductCategory
    total: Decimal