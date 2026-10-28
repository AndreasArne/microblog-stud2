"""Longer password_hash column, Werkzeug 3 scrypt hashes do not fit in 128 characters

Revision ID: b7c1d2e3f4a5
Revises: a524776a1ebb
Create Date: 2026-10-28 15:55:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7c1d2e3f4a5'
down_revision = 'a524776a1ebb'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.String(length=128),
               existing_nullable=True)
