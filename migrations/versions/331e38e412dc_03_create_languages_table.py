"""

03 create languages table

Revision ID: 331e38e412dc
Creation date: 2023-04-21 13:58:27.191141

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '331e38e412dc'
down_revision = 'fee85e90435a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""--sql
        CREATE TABLE languages(
        iso_639_1 TEXT PRIMARY KEY,
        name TEXT
        );
        """
    )


def downgrade() -> None:
    op.execute(
        f"""--sql
        DROP TABLE IF EXISTS languages CASCADE;
        """
    )
