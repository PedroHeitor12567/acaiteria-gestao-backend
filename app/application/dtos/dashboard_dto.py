from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from app.domain.enums.product_catetgory import ProductCategory


@dataclass
class DashboardOutput:
    daily_sales: Decimal
    monthly_sales: Decimal
    monthly_expenses: Decimal
    monthly_profit: Decimal
    closed_commands_count: int
    average_ticket: Decimal
    best_selling_product: Optional[str]
    best_selling_category: Optional[ProductCategory]