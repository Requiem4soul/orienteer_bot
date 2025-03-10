"""economy_rewrite_1

Revision ID: 347c1bbc82c6
Revises: 17df4ce4b5ae
Create Date: 2024-09-10 22:26:25.426090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '347c1bbc82c6'
down_revision: Union[str, None] = '17df4ce4b5ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role_time_coefficients',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('coefficient', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('transaction_type', sa.Enum('Ban', 'Pardon', 'Transfer', 'Promo', 'Boosty', 'Tip', 'Playtime', 'Other', name='transactiontype'), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('role_time_coefficients')
    # ### end Alembic commands ###
