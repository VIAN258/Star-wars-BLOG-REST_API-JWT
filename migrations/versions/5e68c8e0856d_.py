"""empty message

Revision ID: 5e68c8e0856d
Revises: ff33ae20851e
Create Date: 2023-02-21 22:14:22.615881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e68c8e0856d'
down_revision = 'ff33ae20851e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('characters_name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ships_name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('ship_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['ship_id'], ['ship.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('ship_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['ship_id'], ['ship.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('name')

    op.drop_table('favorite')
    op.drop_table('type')
    op.drop_table('ship')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
