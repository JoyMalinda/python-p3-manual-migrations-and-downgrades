"""Renaming students to scholars

Revision ID: 0103b8cde6aa
Revises: 791279dd0760
Create Date: 2025-06-20 10:27:41.747829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0103b8cde6aa'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
