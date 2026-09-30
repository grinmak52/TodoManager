"""create category table

Revision ID: 89c08b42b4dc
Revises: a2f7d4829b5a
Create Date: 2026-09-30 17:10:32.708273

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "89c08b42b4dc"
down_revision: Union[str, Sequence[str], None] = "a2f7d4829b5a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_categories")),
    )


def downgrade() -> None:
    op.drop_table("categories")
