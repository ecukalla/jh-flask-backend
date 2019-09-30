"""Entities bank account/operation/label

Revision ID: 25a9f04cf8ea
Revises: 0977376016cc
Create Date: 2019-09-30 01:51:41.469957

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '25a9f04cf8ea'
down_revision = '0977376016cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    jhi_label = op.create_table('jhi_label',
                                sa.Column('id', sa.Integer(), nullable=False),
                                sa.Column('label', sa.String(), nullable=True),
                                sa.PrimaryKeyConstraint('id')
                                )
    jhi_bank_account = op.create_table('jhi_bank_account',
                                       sa.Column('id', sa.Integer(), nullable=False),
                                       sa.Column('name', sa.String(), nullable=True),
                                       sa.Column('balance', sa.Float(), nullable=True),
                                       sa.Column('user_id', sa.Integer(), nullable=True),
                                       sa.ForeignKeyConstraint(['user_id'], ['jhi_user.uid'], ),
                                       sa.PrimaryKeyConstraint('id')
                                       )
    jhi_operation = op.create_table('jhi_operation',
                                    sa.Column('id', sa.Integer(), nullable=False),
                                    sa.Column('date', sa.DateTime(), nullable=False),
                                    sa.Column('description', sa.String(), nullable=True),
                                    sa.Column('amount', sa.Float(), nullable=False),
                                    sa.Column('bank_account_id', sa.Integer(), nullable=True),
                                    sa.ForeignKeyConstraint(['bank_account_id'], ['jhi_bank_account.id'], ),
                                    sa.PrimaryKeyConstraint('id')
                                    )
    jhi_operation_label = op.create_table('jhi_operation_label',
                                          sa.Column('operation_id', sa.Integer(), nullable=False),
                                          sa.Column('label_id', sa.Integer(), nullable=False),
                                          sa.ForeignKeyConstraint(['label_id'], ['jhi_label.id'], ),
                                          sa.ForeignKeyConstraint(['operation_id'], ['jhi_operation.id'], ),
                                          sa.PrimaryKeyConstraint('operation_id', 'label_id')
                                          )

    op.bulk_insert(jhi_label, [
        {"id": 1, "label": "Yuan Renminbi Centers"},
        {"id": 2, "label": "Factors"},
        {"id": 3, "label": "South Dakota envisioneer Music"},
        {"id": 4, "label": "Nakfa"},
        {"id": 5, "label": "Bahamian Dollar Investment Account"},
        {"id": 6, "label": "Games Regional Digitized"},
        {"id": 7, "label": "copy convergence"},
        {"id": 8, "label": "Mayotte"},
        {"id": 9, "label": "Industrial"},
        {"id": 10, "label": "connect Markets Chief"}
    ])

    op.bulk_insert(jhi_bank_account, [
        {"id": 1, "name": "mobile Fish", "balance": 77969.00, "userId": None},
        {"id": 2, "name": "Savings Account Dam", "balance": 9997.00, "userId": None},
        {"id": 3, "name": "Trace", "balance": 33370.00, "userId": None},
        {"id": 4, "name": "Metal deposit", "balance": 5641.00, "userId": None},
        {"id": 5, "name": "transmitter Implementation Electronics", "balance": 99221.00, "userId": None},
        {"id": 6, "name": "Money Market Account", "balance": 61165.00, "userId": None},
        {"id": 7, "name": "Grocery Home", "balance": 52477.00, "userId": None},
        {"id": 8, "name": "enable Gorgeous Frozen Pants", "balance": 23277.00, "userId": None},
        {"id": 9, "name": "Licensed Savings Account", "balance": 38246.00, "userId": None},
        {"id": 10, "name": "Planner Canyon", "balance": 85994.00, "userId": None}
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jhi_operation_label')
    op.drop_table('jhi_operation')
    op.drop_table('jhi_bank_account')
    op.drop_table('jhi_label')
    # ### end Alembic commands ###
