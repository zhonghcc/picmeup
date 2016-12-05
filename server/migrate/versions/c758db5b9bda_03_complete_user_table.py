"""03 complete user table

Revision ID: c758db5b9bda
Revises: 144639404d09
Create Date: 2016-11-30 14:23:19.717000

"""

# revision identifiers, used by Alembic.
revision = 'c758db5b9bda'
down_revision = '144639404d09'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users',sa.Column('email',sa.String(255),nullable=True))
    op.add_column('users',sa.Column('mobile',sa.String(255),nullable=True))
    op.add_column('users',sa.Column('last_log_ip',sa.String(50),nullable=True))
    pass


def downgrade():
    op.drop_column('users','email')
    op.drop_column('users','mobile')
    op.drop_column('users','last_log_ip')
    pass
