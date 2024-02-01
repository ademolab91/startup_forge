"""empty message

Revision ID: bc5620ef32a5
Revises: 41bd6c231814
Create Date: 2024-02-01 00:15:47.232602

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "bc5620ef32a5"
down_revision = "41bd6c231814"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("language")
    op.drop_table("social_link")
    op.add_column(
        "profile",
        sa.Column("languages", sa.ARRAY(sa.String(), dimensions=2), nullable=True),
    )
    op.add_column(
        "profile",
        sa.Column("social_links", sa.ARRAY(sa.String(), dimensions=2), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("profile", "social_links")
    op.drop_column("profile", "languages")
    op.create_table(
        "social_link",
        sa.Column("user_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "platform",
            postgresql.ENUM(
                "TWITTER",
                "LINKEDIN",
                "FACEBOOK",
                "INSTAGRAM",
                "WHATSAPP",
                name="platform",
            ),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("link", sa.VARCHAR(length=150), autoincrement=False, nullable=False),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="social_link_user_id_fkey",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="social_link_pkey"),
    )
    op.create_table(
        "language",
        sa.Column("user_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "name",
            postgresql.ENUM("ENGLISH", "SPANISH", "ARABIC", name="languagename"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "level",
            postgresql.ENUM("BASIC", "CONVERSATIONAL", "FLUENT", name="languagelevel"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="language_user_id_fkey",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="language_pkey"),
    )
    # ### end Alembic commands ###
