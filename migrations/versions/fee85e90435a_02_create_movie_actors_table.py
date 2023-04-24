"""

02 create movie_actors table

Revision ID: fee85e90435a
Creation date: 2023-04-21 08:43:24.543463

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'fee85e90435a'
down_revision = '8d1d6672dc13'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"""--sql
        CREATE TABLE movie_actors(
        credit_id TEXT NOT NULL UNIQUE PRIMARY KEY,
        movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
        actor_id INT REFERENCES actors(actor_id) ON DELETE CASCADE,
        cast_id INT NOT NULL,
        character TEXT NOT NULL,
        gender INT NOT NULL,
        "order" INT NOT NULL
        );
        """
    )
    # op.execute(
    #     f"""--sql
    #     CREATE TABLE movie_actors(
    #     credit_id TEXT NOT NULL UNIQUE PRIMARY KEY,
    #     movie_id INT NOT NULL,
    #     actor_id INT NOT NULL,
    #     cast_id INT NOT NULL,
    #     character TEXT NOT NULL,
    #     gender INT NOT NULL,
    #     "order" INT NOT NULL
    #     );
    #     """
    # )


def downgrade() -> None:
    op.execute(
        f"""--sql
        DROP TABLE IF EXISTS movie_actors CASCADE;
        """
    )
