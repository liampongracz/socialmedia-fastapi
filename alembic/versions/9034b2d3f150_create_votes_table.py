"""create votes table

Revision ID: 9034b2d3f150
Revises: 1e429f96af83
Create Date: 2021-12-02 00:01:29.453105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9034b2d3f150'
down_revision = '1e429f96af83'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes')
    pass


def downgrade():
    op.drop_table('votes')
    pass
