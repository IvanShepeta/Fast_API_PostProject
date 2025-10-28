"""add user table

Revision ID: d547842f4131
Revises: b96ce96d6ad6
Create Date: 2025-10-28 12:47:29.895638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd547842f4131'
down_revision: Union[str, Sequence[str], None] = 'b96ce96d6ad6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column("id", sa.Integer, nullable=False),
                    sa.Column("email", sa.String, nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text("NOW()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
