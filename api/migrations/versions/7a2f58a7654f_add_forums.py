"""ADD forums

Revision ID: 7a2f58a7654f
Revises: a143a9fa5199
Create Date: 2022-01-15 00:14:59.294251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7a2f58a7654f"
down_revision = "a143a9fa5199"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "forum_category",
        sa.Column("id", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=True),
        sa.Column("course_id", sa.String(length=128), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    op.create_table(
        "forum_post",
        sa.Column("id", sa.String(length=128), nullable=False),
        sa.Column("owner_id", sa.String(length=128), nullable=False),
        sa.Column("course_id", sa.String(length=128), nullable=True),
        sa.Column("visible_to_students", sa.Boolean(), nullable=True),
        sa.Column("pinned", sa.Boolean(), nullable=True),
        sa.Column("anonymous", sa.Boolean(), nullable=True),
        sa.Column("seen_count", sa.Integer(), nullable=True),
        sa.Column("title", sa.TEXT(length=1024), nullable=True),
        sa.Column("content", sa.TEXT(length=16384), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    op.create_table(
        "forum_post_comment",
        sa.Column("id", sa.String(length=128), nullable=False),
        sa.Column("owner_id", sa.String(length=128), nullable=False),
        sa.Column("post_id", sa.String(length=128), nullable=False),
        sa.Column("next_id", sa.String(length=128), nullable=True),
        sa.Column("approved_by_id", sa.String(length=128), nullable=True),
        sa.Column("anonymous", sa.Boolean(), nullable=True),
        sa.Column("thread_start", sa.Boolean(), nullable=True),
        sa.Column("content", sa.TEXT(length=4096), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["approved_by_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    op.create_table(
        "forum_post_in_category",
        sa.Column("post_id", sa.String(length=128), nullable=False),
        sa.Column("category_id", sa.String(length=128), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["forum_category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("post_id", "category_id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    op.create_table(
        "forum_post_upvote",
        sa.Column("id", sa.String(length=128), nullable=False),
        sa.Column("owner_id", sa.String(length=128), nullable=False),
        sa.Column("post_id", sa.String(length=128), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("id", "owner_id", "post_id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    op.create_table(
        "forum_post_viewed",
        sa.Column("owner_id", sa.String(length=128), nullable=False),
        sa.Column("post_id", sa.String(length=128), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("owner_id", "post_id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("forum_post_viewed")
    op.drop_table("forum_post_upvote")
    op.drop_table("forum_post_in_category")
    op.drop_table("forum_post_comment")
    op.drop_table("forum_post")
    op.drop_table("forum_category")
    # ### end Alembic commands ###
