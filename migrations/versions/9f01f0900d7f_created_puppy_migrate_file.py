"""created puppy migrate file

Revision ID: 9f01f0900d7f
Revises: 
Create Date: 2024-01-15 18:13:35.270573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f01f0900d7f'
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
    op.drop_table('puppy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('puppies')
    # ### end Alembic commands ###