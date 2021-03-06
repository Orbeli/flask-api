"""empty message

Revision ID: bc17b31d1850
Revises: ddb5ec5e3eff
Create Date: 2021-09-11 21:12:29.709366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc17b31d1850'
down_revision = 'ddb5ec5e3eff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funcionario_projeto',
    sa.Column('projeto_id', sa.Integer(), nullable=False),
    sa.Column('funcionario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('projeto_id', 'funcionario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionario_projeto')
    # ### end Alembic commands ###
