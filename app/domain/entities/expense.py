from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

from datetime import datetime


@dataclass
class Expense:
    id: Optional[int]
    description: str
    value: Decimal
    date: datetime