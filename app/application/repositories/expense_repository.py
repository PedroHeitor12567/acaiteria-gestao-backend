from abc import ABC, abstractmethod
from datetime import datetime

from app.domain.entities.expense import Expense


class ExpenseRepository(ABC):
    @abstractmethod
    def create(self, expense: Expense) -> Expense: ...

    @abstractmethod
    def list_all(self) -> list[Expense]: ...

    @abstractmethod
    def list_between(self, start: datetime, end: datetime) -> list[Expense]: ...