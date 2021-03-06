"""empty message

Revision ID: 4cb532fedcf8
Revises: 97db95a71bca
Create Date: 2019-08-07 11:43:36.640382

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4cb532fedcf8'
down_revision = '97db95a71bca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_tags_rls',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['article_tags.id'], ),
    sa.PrimaryKeyConstraint('article_id', 'tag_id')
    )
    op.drop_table('article_categories_rls')
    op.drop_constraint('article_tags_ibfk_1', 'article_tags', type_='foreignkey')
    op.drop_column('article_tags', 'article')
    op.add_column('articles', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'articles', 'article_categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_column('articles', 'category_id')
    op.add_column('article_tags', sa.Column('article', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('article_tags_ibfk_1', 'article_tags', 'articles', ['article'], ['id'])
    op.create_table('article_categories_rls',
    sa.Column('article_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('category_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], name='article_categories_rls_ibfk_1'),
    sa.ForeignKeyConstraint(['category_id'], ['article_categories.id'], name='article_categories_rls_ibfk_2'),
    sa.PrimaryKeyConstraint('article_id', 'category_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('article_tags_rls')
    # ### end Alembic commands ###
