"""create article,tag,user,article_like table

Revision ID: 89f1b12b571b
Revises: 
Create Date: 2016-08-09 09:42:52.764000

"""

# revision identifiers, used by Alembic.
revision = '89f1b12b571b'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from datetime import datetime

def upgrade():


    op.create_table(
        'articles',
        sa.Column('id',sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('title',sa.String(255), nullable=False),
        sa.Column('description',sa.Text,nullable=True),
        sa.Column('origin',sa.String(255),nullable=True),
        sa.Column('file_name',sa.String(255),nullable=True),
        sa.Column('origin_url',sa.Text,nullable=True),
        sa.Column('pic_url',sa.Text,nullable=True),

        sa.Column('created_time',sa.DateTime, default=datetime.now),
        sa.Column('updated_time',sa.DateTime, default=datetime.now),
        sa.Column('status',sa.Integer, nullable=False),
        sa.Column('order',sa.Integer,nullable=True,default=0)
    )
    op.create_table(
        'tags',
        sa.Column('id',sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('title',sa.String(255), nullable=False),
        sa.Column('description',sa.Text,nullable=True),
        sa.Column('article_id',sa.Integer,nullable=True),
        sa.Column('author_id',sa.Integer,nullable=True),

        sa.Column('created_time',sa.DateTime, default=datetime.now),
        sa.Column('updated_time',sa.DateTime, default=datetime.now),
        sa.Column('status',sa.Integer, nullable=False),
        sa.Column('order',sa.Integer,nullable=True,default=0)
    )

    op.create_table(
        'users',
        sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
        sa.Column('username',sa.String(255), nullable=False,unique=True),
        sa.Column('nickname',sa.String(255),nullable=False),
        sa.Column('password',sa.String(255), nullable=False),
        sa.Column('last_log_time',sa.DateTime,nullable=True),

        sa.Column('created_time',sa.DateTime, default=datetime.now),
        sa.Column('updated_time',sa.DateTime, default=datetime.now),
        sa.Column('status',sa.Integer, nullable=False),
    )

def downgrade():
    op.drop_table('accounts')

