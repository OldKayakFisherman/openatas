"""Added notifications

Revision ID: f180d17ae699
Revises: bf1086df9b28
Create Date: 2024-03-11 17:15:59.310240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f180d17ae699'
down_revision = 'bf1086df9b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host', sa.String(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('severity', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('whencreated', sa.DateTime(), nullable=True),
    sa.Column('whocreated', sa.String(), nullable=True),
    sa.Column('success', sa.Boolean(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('request_headers', sa.String(), nullable=True),
    sa.Column('clientversion', sa.String(), nullable=True),
    sa.Column('backendversion', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('event_logs', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_event_logs_id'), ['id'], unique=False)

    op.create_table('notification_queue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=40), nullable=True),
    sa.Column('date_sent', sa.DateTime(), nullable=True),
    sa.Column('date_queued', sa.DateTime(), nullable=True),
    sa.Column('subject', sa.Text(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notification_queue_attachments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mime_type', sa.String(length=40), nullable=True),
    sa.Column('extension', sa.String(length=10), nullable=True),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.Column('filecontents', sa.LargeBinary(), nullable=True),
    sa.Column('notification_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['notification_id'], ['operating_divisions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('approved', sa.Boolean(), nullable=True))
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.alter_column('username',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
        batch_op.drop_column('approved')
        batch_op.drop_column('password_hash')
        batch_op.drop_column('email')

    op.drop_table('notification_queue_attachments')
    op.drop_table('notification_queue')
    with op.batch_alter_table('event_logs', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_event_logs_id'))

    op.drop_table('event_logs')
    # ### end Alembic commands ###
