"""add last few columns to post table

Revision ID: fda4c3b43ad4
Revises: 181b591fe99e
Create Date: 2022-01-12 13:21:38.423932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda4c3b43ad4'
down_revision = '181b591fe99e'
branch_labels = None
depends_on = None




def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'))

    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass