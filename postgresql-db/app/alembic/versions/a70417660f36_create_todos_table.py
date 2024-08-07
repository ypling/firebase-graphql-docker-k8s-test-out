"""create todos table

Revision ID: a70417660f36
Revises: 
Create Date: 2024-07-22 14:58:11.535299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a70417660f36'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("create schema api")
    op.create_table(
            'todos',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('done', sa.Boolean, nullable=False, default=False),
            sa.Column('task', sa.Text, nullable=False),
            sa.Column('due', sa.DateTime(timezone=True)),
            schema='api'
        )

def downgrade() -> None:
    op.drop_table(
        'todos',
        schema='api'
        )
    op.execute("drop schema api")
