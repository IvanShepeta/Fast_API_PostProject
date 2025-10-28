"""add content column to posts table

Revision ID: b96ce96d6ad6
Revises: 5206b00ebdc5
Create Date: 2025-10-28 12:41:40.543321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b96ce96d6ad6'
down_revision: Union[str, Sequence[str], None] = '5206b00ebdc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
