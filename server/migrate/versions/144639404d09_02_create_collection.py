"""02 create collection

Revision ID: 144639404d09
Revises: b1cb970952e2
Create Date: 2016-09-21 15:26:07.778000

"""

# revision identifiers, used by Alembic.
revision = '144639404d09'
down_revision = 'b1cb970952e2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from datetime import datetime



def upgrade():
    op.create_table(
        'collections',
        sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
        sa.Column('name',sa.String(255), nullable=False,unique=True),

        sa.Column('created_time',sa.DateTime, default=datetime.now),
        sa.Column('updated_time',sa.DateTime, default=datetime.now),

        sa.Column('author_id',sa.Integer,nullable=True),
        sa.Column('status',sa.Integer, nullable=False),
        sa.Column('order',sa.Integer,nullable=True,default=0)
    )
    op.create_table(
        'collection_items',
        sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
        sa.Column('collection_id',sa.Integer,nullable=True),
        sa.Column('article_id',sa.Integer,nullable=True),

        sa.Column('created_time',sa.DateTime, default=datetime.now),
        sa.Column('updated_time',sa.DateTime, default=datetime.now),

        sa.Column('status',sa.Integer, nullable=False),
        sa.Column('order',sa.Integer,nullable=True,default=0)
    )


def downgrade():
    op.drop_table('collections')
    op.drop_table('collection_items')
