"""

03 import movies into movies table

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
    pass
    # for i in range(movie_table_length()):
        # op.execute(
        #     f"""--sql
        #     INSERT INTO movies(movie_id, title) VALUES {import_movie(i)};
        #     """
        # )


def downgrade() -> None:
    pass
    # op.execute(
    #     f"""--sql
    #     TRUNCTUATE movies CASCADE;
    #     """
    #     # DELETE FROM movies;
    # )
