"""empty message

Revision ID: 9188d57ca99b
Revises: 
Create Date: 2021-09-29 07:28:25.654411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9188d57ca99b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('appointment_location', sa.String(length=200), nullable=True),
    sa.Column('appointment_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('location')
    # ### end Alembic commands ###
