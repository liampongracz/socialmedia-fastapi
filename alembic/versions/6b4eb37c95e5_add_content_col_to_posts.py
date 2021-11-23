"""add content col to posts

Revision ID: 6b4eb37c95e5
Revises: d5f90b74947b
Create Date: 2021-11-20 14:01:56.295399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b4eb37c95e5'
down_revision = 'd5f90b74947b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
