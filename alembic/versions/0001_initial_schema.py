import sqlalchemy as sa

from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    product_category = sa.Enum("ACAI", "SORVETE", "GUARACAI", "OUTROS", name="product_category")
    command_status = sa.Enum("OPEN", "CLOSED", "CANCELED", name="command_status")

    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("category", product_category, nullable=False),
        sa.Column("sale_price", sa.Numeric(10, 2), nullable=False),
        sa.Column("cost_price", sa.Numeric(10, 2), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
    )

    op.create_table(
        "commands",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("command_number", sa.Integer(), nullable=False, unique=True),
        sa.Column("opened_at", sa.DateTime(), nullable=False),
        sa.Column("closed_at", sa.DateTime(), nullable=True),
        sa.Column("status", command_status, nullable=False, server_default="OPEN"),
        sa.Column("total", sa.Numeric(10, 2), nullable=False, server_default="0.00"),
    )

    op.create_table(
        "command_items",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("command_id", sa.Integer(), sa.ForeignKey("commands.id"), nullable=False),
        sa.Column("product_id", sa.Integer(), sa.ForeignKey("products.id"), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("unit_price", sa.Numeric(10, 2), nullable=False),
        sa.Column("subtotal", sa.Numeric(10, 2), nullable=False),
    )

    op.create_table(
        "expenses",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("value", sa.Numeric(10, 2), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table("command_items")
    op.drop_table("commands")
    op.drop_table("expenses")
    op.drop_table("products")
    sa.Enum(name="command_status").drop(op.get_bind(), checkfirst=True)
    sa.Enum(name="product_category").drop(op.get_bind(), checkfirst=True)