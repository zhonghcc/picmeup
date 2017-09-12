"""04 add user like mark view

Revision ID: 0b4e58b9c237
Revises: c758db5b9bda
Create Date: 2017-09-12 11:18:04.591000

"""

# revision identifiers, used by Alembic.
revision = '0b4e58b9c237'
down_revision = 'c758db5b9bda'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from datetime import datetime


def upgrade():
    op.create_table(
            'article_like',
            sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
            sa.Column('article_id',sa.Integer, nullable=False),
            sa.Column('user_id',sa.Integer, nullable=False),

            sa.Column('created_time',sa.DateTime, default=datetime.now),
            sa.Column('updated_time',sa.DateTime, default=datetime.now),

            sa.Column('status',sa.Integer, nullable=False),
    )



    op.create_table(
            'article_view',
            sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
            sa.Column('article_id',sa.Integer, nullable=False),
            sa.Column('user_id',sa.Integer, nullable=True),
            sa.Column('ip',sa.String(50), nullable=True),

            sa.Column('created_time',sa.DateTime, default=datetime.now),
            sa.Column('updated_time',sa.DateTime, default=datetime.now),

            sa.Column('status',sa.Integer, nullable=False),
    )

    op.create_table(
            'article_download',
            sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
            sa.Column('article_id',sa.Integer, nullable=False),
            sa.Column('user_id',sa.Integer, nullable=True),
            sa.Column('ip',sa.String(50), nullable=True),

            sa.Column('created_time',sa.DateTime, default=datetime.now),
            sa.Column('updated_time',sa.DateTime, default=datetime.now),

            sa.Column('status',sa.Integer, nullable=False),
    )
    op.add_column('articles',sa.Column('view_num',sa.Integer,nullable=False,default=0))
    op.add_column('articles',sa.Column('like_num',sa.Integer,nullable=False,default=0))
    op.add_column('articles',sa.Column('download_num',sa.Integer,nullable=False,default=0))
    pass


def downgrade():
    op.drop_table('article_like')
    op.drop_table('article_view')
    op.drop_table('article_download')
    op.drop_column('articles','view_num')
    op.drop_column('articles','like_num')
    op.drop_column('articles','download_num')
    pass
