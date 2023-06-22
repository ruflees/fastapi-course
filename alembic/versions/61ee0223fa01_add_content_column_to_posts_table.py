"""add content column to posts table

Revision ID: 61ee0223fa01
Revises: cc5028d32722
Create Date: 2023-06-14 20:25:59.901135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61ee0223fa01'
down_revision = 'cc5028d32722'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=True))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
