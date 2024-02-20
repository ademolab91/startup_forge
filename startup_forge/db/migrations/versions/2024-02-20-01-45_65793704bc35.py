"""empty message

Revision ID: 65793704bc35
Revises: e12d8d6a6d90
Create Date: 2024-02-20 01:45:22.304181

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "65793704bc35"
down_revision = "e12d8d6a6d90"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comment_reply",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("comment_id", sa.Uuid(), nullable=False),
        sa.Column("reply_id", sa.Uuid(), nullable=True),
        sa.ForeignKeyConstraint(
            ["comment_id"], ["comment.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["reply_id"], ["comment.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("comment_reply")
    # ### end Alembic commands ###