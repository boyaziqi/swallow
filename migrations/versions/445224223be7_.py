"""empty message

Revision ID: 445224223be7
Revises: dbf9dbed0991
Create Date: 2019-08-05 17:11:48.339926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '445224223be7'
down_revision = 'dbf9dbed0991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tags')
    op.drop_table('article_categories')
    # ### end Alembic commands ###
