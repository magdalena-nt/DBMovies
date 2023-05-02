from asyncio import run, sleep

from src.movies.analysis_tools import get_movie_keywords
from src.movies.db_service import DbService


async def main():
    db = DbService()
    await db.initialize()

    keywords = get_movie_keywords('data/tmdb_5000_movies.csv')

    for i, keyword in enumerate(keywords):
        await db.upsert_moviekeyword(keyword)
        if i % 100 == 0:
            print(f'import in {i / len(keywords) * 100:.1f}% done')

    await sleep(1)
    print('upsert moviekeywords done')


if __name__ == '__main__':
    run(main())
