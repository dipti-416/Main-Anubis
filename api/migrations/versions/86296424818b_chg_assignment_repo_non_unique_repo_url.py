"""CHG assignment_repo non unique repo_url

Revision ID: 86296424818b
Revises: fff88033d4f9
Create Date: 2021-08-25 00:15:55.283501

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "86296424818b"
down_revision = "fff88033d4f9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("repo_url", table_name="assignment_repo")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("repo_url", "assignment_repo", ["repo_url"], unique=False)
    # ### end Alembic commands ###
