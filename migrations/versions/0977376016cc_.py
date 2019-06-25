"""create users, authorities, and insert fixtures

Revision ID: 0977376016cc
Revises:
Create Date: 2019-06-21 17:48:40.745230

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0977376016cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    jhi_authority = op.create_table('jhi_authority',
                                    sa.Column('id', sa.Integer(), nullable=False),
                                    sa.Column('name', sa.String(length=50), nullable=False),
                                    sa.PrimaryKeyConstraint('id', 'name')
                                    )

    jhi_user = op.create_table('jhi_user',
                               sa.Column('uid', sa.BigInteger(), nullable=False),
                               sa.Column('login', sa.String(length=50), nullable=False),
                               sa.Column('password_hash', sa.String(length=60), nullable=True),
                               sa.Column('first_name', sa.String(length=50), nullable=True),
                               sa.Column('last_name', sa.String(length=50), nullable=True),
                               sa.Column('email', sa.String(length=191), nullable=True),
                               sa.Column('image_url', sa.String(length=256), nullable=True),
                               sa.Column('activated', sa.Boolean(), nullable=True),
                               sa.Column('lang_key', sa.String(length=10), nullable=True),
                               sa.Column('activation_key', sa.String(length=20), nullable=True),
                               sa.Column('reset_key', sa.String(length=20), nullable=True),
                               sa.Column('created_by', sa.String(length=50), nullable=True),
                               sa.Column('created_date', sa.DateTime(), nullable=True),
                               sa.Column('reset_date', sa.DateTime(), nullable=True),
                               sa.Column('last_modified_by', sa.String(length=50), nullable=True),
                               sa.Column('last_modified_date', sa.DateTime(), nullable=True),
                               sa.PrimaryKeyConstraint('uid'),
                               sa.UniqueConstraint('login')
                               )

    jhi_user_authority = op.create_table('jhi_user_authority',
                                         sa.Column('user_id', sa.BigInteger(), nullable=False),
                                         sa.Column('authority_name', sa.String(length=50), nullable=False),
                                         sa.ForeignKeyConstraint(('authority_name',), ['jhi_authority.name'], ),
                                         sa.ForeignKeyConstraint(('user_id',), ['jhi_user.uid'], ),
                                         sa.PrimaryKeyConstraint('user_id', 'authority_name')
                                         )

    op.bulk_insert(jhi_authority, [
        {'name': 'ROLE_ADMIN'},
        {'name': 'ROLE_USER'}
    ])

    op.bulk_insert(jhi_user, [
        {
            'id': 1,
            'login': 'system',
            'password_hash': '$2a$10$mE.qmcV0mFU5NcKh73TZx.z4ueI/.bDWbj0T1BYyqP481kGGarKLG',
            'first_name': 'System',
            'last_name': 'System',
            'email': 'system@localhost',
            'activated': True,
            'lang_key': 'en',
            'created_by': 'system',
            'last_modified_by': 'system'
        },
        {
            'id': 2,
            'login': 'anonymoususer',
            'password_hash': '$2a$10$j8S5d7Sr7.8VTOYNviDPOeWX8KcYILUVJBsYV83Y5NtECayypx9lO',
            'first_name': 'Anonymous',
            'last_name': 'User',
            'email': 'anonymous@localhost',
            'activated': True,
            'lang_key': 'en',
            'created_by': 'system',
            'last_modified_by': 'system'
        },
        {
            'id': 4,
            'login': 'user',
            'password_hash': '$2a$10$VEjxo0jq2YG9Rbk2HmX9S.k1uZBGYUHdUcid3g/vfiEl7lwWgOH/K',
            'first_name': 'User',
            'last_name': 'User',
            'email': 'user@localhost',
            'activated': True,
            'lang_key': 'en',
            'created_by': 'system',
            'last_modified_by': 'system'
        },
    ])

    op.bulk_insert(jhi_user_authority, [
        {'user_id': 1, 'authority_name': 'ROLE_ADMIN'},
        {'user_id': 1, 'authority_name': 'ROLE_USER'},
        {'user_id': 3, 'authority_name': 'ROLE_ADMIN'},
        {'user_id': 3, 'authority_name': 'ROLE_USER'},
        {'user_id': 4, 'authority_name': 'ROLE_USER'}
    ])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jhi_user_authority')
    op.drop_table('jhi_user')
    op.drop_table('jhi_authority')
    # ### end Alembic commands ###
