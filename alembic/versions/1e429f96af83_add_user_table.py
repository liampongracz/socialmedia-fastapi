"""add user table

Revision ID: 1e429f96af83
Revises: 157d27ab622d
Create Date: 2021-12-01 23:55:30.731784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e429f96af83'
down_revision = '157d27ab622d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('email',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('users')
    pass
