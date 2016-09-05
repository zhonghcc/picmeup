"""01 user desc (author)

Revision ID: b1cb970952e2
Revises: 89f1b12b571b
Create Date: 2016-08-30 10:33:34.271000

"""

# revision identifiers, used by Alembic.
revision = 'b1cb970952e2'
down_revision = '89f1b12b571b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    op.add_column('users',sa.Column('origin',sa.String(255),nullable=True))
    op.add_column('users',sa.Column('origin_url',sa.Text,nullable=True))
    op.add_column('users',sa.Column('description',sa.Text,nullable=True))
    op.add_column('users',sa.Column('role',sa.String(255),nullable=True))
    op.add_column('users',sa.Column('is_imported',sa.Boolean,nullable=True))
    op.add_column('articles',sa.Column('author_id',sa.Integer,nullable=True))

    op.alter_column('users','password',nullable=True,existing_type=mysql.VARCHAR(255))
    pass


def downgrade():
    op.drop_column('users','description')
    op.drop_column('users','origin')
    op.drop_column('users','origin_url')
    op.drop_column('users','role')
    op.drop_column('users','is_imported')
    op.drop_column('articles','author_id')

    op.alter_column('users','password',nullable=True,existing_type=mysql.VARCHAR(255))
    pass
