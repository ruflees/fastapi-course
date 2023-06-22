"""add last few columns to posts table

Revision ID: 3bf0129ee27e
Revises: 7eee96203503
Create Date: 2023-06-15 18:56:48.273077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bf0129ee27e'
down_revision = '7eee96203503'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('viewable', sa.Boolean(), server_default=sa.text('TRUE'), nullable=False),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                              server_default=sa.text('now()')),)
    op.add_column('posts', sa.Column('edited', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),)
    
    pass


def downgrade():
    op.drop_column('posts', 'viewable')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'edited')

    pass
