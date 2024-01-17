"""db init and migrate setup

Revision ID: 62302fa3d783
Revises: 
Create Date: 2024-01-17 14:27:01.339447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62302fa3d783'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
