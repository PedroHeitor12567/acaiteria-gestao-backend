from datetime import datetime
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from app.domain.enums.command_status import CommandStatus
from command_item import CommandItem


@dataclass
class Command:
    id: Optional[int]
    command_number: int
    opened_at: datetime
    closed_at: Optional[datetime]
    status: CommandStatus
    total: Decimal
    items: list[CommandItem] = field(default_factory=list)