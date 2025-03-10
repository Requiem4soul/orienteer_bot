"""user_id_unique_fix

Revision ID: f12096c7fb71
Revises: b7d9c3dfebf3
Create Date: 2024-07-26 18:27:21.425502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f12096c7fb71'
down_revision: Union[str, None] = 'b7d9c3dfebf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('promotional_code_usages_user_id_key', 'promotional_code_usages', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('promotional_code_usages_user_id_key', 'promotional_code_usages', ['user_id'])
    # ### end Alembic commands ###
