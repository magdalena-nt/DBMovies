"""

00 create movies table

Revision ID: 1bfbf5c1067b
Creation date: 2023-04-21 08:37:44.893617

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '1bfbf5c1067b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""--sql
        CREATE TABLE movies(
        movie_id INT PRIMARY KEY,
        title TEXT NOT NULL
        );
        """
    )


def downgrade() -> None:
    op.execute(
        f"""--sql
        DROP TABLE IF EXISTS movies CASCADE;
        """
    )
