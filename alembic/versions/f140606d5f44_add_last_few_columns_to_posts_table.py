"""add last few columns to posts table

Revision ID: f140606d5f44
Revises: 3076d24eec7d
Create Date: 2025-10-28 14:19:39.103120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f140606d5f44'
down_revision: Union[str, Sequence[str], None] = '3076d24eec7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text("NOW()")), )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
