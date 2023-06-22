"""create posts table

Revision ID: cc5028d32722
Revises: 
Create Date: 2023-06-14 20:06:10.809281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc5028d32722'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('text', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
