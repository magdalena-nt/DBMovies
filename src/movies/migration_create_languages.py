from asyncio import run

from analysis_tools import get_languages
from db_service import DbService


async def create_languages():
    db = DbService()
    await db.initialize()

    languages_ = get_languages()

    print(f'all languages: {len(languages_)}')
    for l in languages_:
        await db.upsert_language(l)


if __name__ == '__main__':
    run(create_languages())
