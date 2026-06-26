from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy import Enum as SAEnum

from app.domain.enums import CommandStatus, ProductCategory

class Base(DeclarativeBase):
    pass

class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    category: Mapped[ProductCategory] = mapped_column(
        SAEnum(ProductCategory, name="product_category"), nullable=False
    )
    sale_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    cost_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    items: Mapped[list["CommandItemModel"]] = relationship(back_populates="product")

class CommandModel(Base):
    __tablename__ = "commands"

    id: Mapped[int] = mapped_column(primary_key=True)
    command_number: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    opened_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    status: Mapped[CommandStatus] = mapped_column(
        SAEnum(CommandStatus, name="command_status"), nullable=False, default=CommandStatus.OPEN
    )
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))

    items: Mapped[list["CommandItemModel"]] = relationship(
        back_populates="command", cascade="all, delete-orphan"
    )

class CommandItemModel(Base):
    __tablename__ = "command_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    command_id: Mapped[int] = mapped_column(ForeignKey("commands.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    command: Mapped["CommandModel"] = relationship(back_populates="items")
    product: Mapped["ProductModel"] = relationship(back_populates="items")

class ExpenseModel(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)