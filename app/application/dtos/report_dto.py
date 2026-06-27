from dataclasses import dataclass, field
from decimal import Decimal
from sales_dto import CategorySalesOutput

@dataclass
class MonthlyReportOutput:
    month: int
    year: int
    gross_revenue: Decimal
    expenses: Decimal
    net_profit: Decimal
    closed_commands_count: int
    sales_by_category: list[CategorySalesOutput] = field(default_factory=list)