"""

05 create movie keywords table

Revision ID: 56b02166915a
Creation date: 2023-04-29 13:10:18.408271

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '56b02166915a'
down_revision = '1e0476122564'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""--sql
        CREATE TABLE movie_keywords(
        movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
        keyword_id INT REFERENCES keywords(keyword_id) ON DELETE CASCADE
        );
        """
    )


def downgrade() -> None:
    op.execute(
        f"""--sql
        DROP TABLE IF EXISTS movie_keywords CASCADE;
        """
    )
