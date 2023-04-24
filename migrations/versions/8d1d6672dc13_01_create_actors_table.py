"""

01 create actors table

Revision ID: 8d1d6672dc13
Creation date: 2023-04-21 08:41:58.557466

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '8d1d6672dc13'
down_revision = '1bfbf5c1067b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""--sql
        CREATE TABLE actors(
        actor_id INT PRIMARY KEY,
        name TEXT NOT NULL
        );
        """
    )


def downgrade() -> None:
    op.execute(
        f"""--sql
        DROP TABLE IF EXISTS actors CASCADE;
        """
    )
