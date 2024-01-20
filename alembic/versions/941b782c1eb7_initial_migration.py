"""initial migration

Revision ID: 941b782c1eb7
Revises: 6c3469d0e392
Create Date: 2024-01-20 12:42:02.266074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '941b782c1eb7'
down_revision: Union[str, None] = '6c3469d0e392'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
