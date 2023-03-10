"""First migrate

Revision ID: 57e3d9cc19d5
Revises: 
Create Date: 2023-01-25 11:47:19.103758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57e3d9cc19d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('driver', sa.String(length=100), nullable=False),
    sa.Column('num_of_car', sa.String(length=100), nullable=False),
    sa.Column('on_line', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cars'))
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_of_car', sa.String(length=100), nullable=False),
    sa.Column('driver', sa.String(length=100), nullable=False),
    sa.Column('client', sa.String(length=100), nullable=False),
    sa.Column('destination', sa.String(length=100), nullable=False),
    sa.Column('num_of_phone', sa.String(length=100), nullable=False),
    sa.Column('sms_code', sa.String(length=100), nullable=False),
    sa.Column('time', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('cars')
    # ### end Alembic commands ###
