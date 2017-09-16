"""05 tag and collection

Revision ID: b5b843df7bcb
Revises: 0b4e58b9c237
Create Date: 2017-09-16 17:44:16.847000

"""

# revision identifiers, used by Alembic.
revision = 'b5b843df7bcb'
down_revision = '0b4e58b9c237'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from datetime import datetime


def upgrade():
    op.drop_column('tags','author_id')
    op.add_column('tags',sa.Column('user_id',sa.Integer,nullable=True,default=0))
    op.add_column('users',sa.Column('coin_num',sa.Integer,nullable=False,default=5))
    op.create_table(
            'coins',
            sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
            sa.Column('direction',sa.String(50),nullable=False,default=""),
            sa.Column('reason',sa.String(50),nullable=False,default=""),
            sa.Column('article_id',sa.Integer, nullable=True),
            sa.Column('user_id',sa.Integer, nullable=True),
            sa.Column('ip',sa.String(50), nullable=True),
            sa.Column('coin_num',sa.Integer, nullable=False,default=0),

            sa.Column('created_time',sa.DateTime, default=datetime.now),
            sa.Column('updated_time',sa.DateTime, default=datetime.now),

            sa.Column('status',sa.Integer, nullable=False),
    )
    pass


def downgrade():
    op.drop_column('tags','user_id')
    op.add_column('tags',sa.Column('author_id',sa.Integer,nullable=True,default=0))
    op.drop_column('users','coin_num')
    op.drop_table('coins')
    pass
