from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

@dataclass
class CreateExpenseInput:
    description: str
    value: Decimal
    date: datetime