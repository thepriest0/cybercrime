"""Add evidence_filename column to Report model

Revision ID: 82e649e6330c
Revises: adab2072ed36
Create Date: 2024-06-06 00:33:25.192394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82e649e6330c'
down_revision = 'adab2072ed36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.add_column(sa.Column('evidence_filename', sa.String(length=200), nullable=True))
        batch_op.drop_column('evidence_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.add_column(sa.Column('evidence_file', sa.VARCHAR(length=200), nullable=True))
        batch_op.drop_column('evidence_filename')

    # ### end Alembic commands ###