"""add image and timeslot classes

Revision ID: eaf25408e763
Revises: 6381d69930e8
Create Date: 2018-07-03 12:44:18.996106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaf25408e763'
down_revision = '6381d69930e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('bedrooms', sa.String(length=255), nullable=True),
    sa.Column('pricing', sa.Integer(), nullable=True),
    sa.Column('lister_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lister_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=25), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('listings')
    # ### end Alembic commands ###