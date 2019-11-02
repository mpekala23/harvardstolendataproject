"""empty message

Revision ID: 82cacfa14890
Revises: 92e2a3f23e3b
Create Date: 2019-10-26 01:25:38.762682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82cacfa14890'
down_revision = '92e2a3f23e3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'category')
    # ### end Alembic commands ###
