"""

04 create keywords table

Revision ID: 1e0476122564
Creation date: 2023-04-28 21:59:41.782882

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '1e0476122564'
down_revision = '331e38e412dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""--sql
        CREATE TABLE keywords(
        keyword_id INT PRIMARY KEY,
        name TEXT
        );
        """
    )


def downgrade() -> None:
    op.execute(
        f"""--sql
        DROP TABLE IF EXISTS keywords CASCADE;
        """
    )
