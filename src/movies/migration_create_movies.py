from asyncio import run

from analysis_tools import get_movies
from db_service import DbService


async def create_movies():
    db = DbService()
    await db.initialize()

    movies = get_movies('data/tmdb_5000_movies.csv')
    print(f'all movies: {len(movies)}')

    for i, m in enumerate(movies):
        # for i,m in enumerate(movies[500:1500]):
        await db.upsert_movie(m)
        if i % 100 == 0:
            print(f'import in {i / len(movies) * 100:.1f}% done')


if __name__ == '__main__':
    run(create_movies())
