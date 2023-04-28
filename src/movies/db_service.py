from asyncio import run
from os import getenv

import asyncpg
from dotenv import load_dotenv

from model import Actor, Movie, Language, Keyword

load_dotenv()
URL = getenv('DATABASE_URL')
SCHEMA = getenv('SCHEMA')


class DbService:

    async def initialize(self):
        self.pool = await asyncpg.create_pool(URL, timeout=30, command_timeout=5,
                                              server_settings={'search_path': SCHEMA})

        print('connected!')

    async def get_actors(self, offset=0, limit=500) -> list[Actor]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from actors order by name offset $1 limit $2', offset, limit)
        return [Actor(**dict(r)) for r in rows]

    async def get_actor(self, actor_id: int) -> Actor | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from actors where actor_id=$1', actor_id)
        return Actor(**dict(row)) if row else None

    async def upsert_actor(self, actor: Actor) -> Actor:
        if actor.actor_id is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into actors(name) VALUES ($1) returning *",
                                                actor.name)
        elif await self.get_actor(actor.actor_id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into actors(actor_id,name) VALUES ($1,$2) returning *",
                                                actor.actor_id, actor.name)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update actors set name=$2 where actor_id=$1 returning *""",
                                                actor.actor_id, actor.name)

        return Actor(**dict(row))

    async def get_movies(self, offset=0, limit=500) -> list[Movie]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from movies order by title offset $1 limit $2', offset, limit)
        return [Movie(**dict(r)) for r in rows]

    async def get_movie(self, movie_id: int) -> Movie | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from movies where movie_id=$1', movie_id)
        return Movie(**dict(row)) if row else None

    async def upsert_movie(self, movie: Movie) -> Movie:
        if movie.movie_id is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into movies(title) VALUES ($1) returning *",
                                                movie.title)
        elif await self.get_movie(movie.movie_id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into movies(movie_id,title) VALUES ($1,$2) returning *",
                                                movie.movie_id, movie.title)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update movies set title=$2 where movie_id=$1 returning *""",
                                                movie.movie_id, movie.title)

        return Movie(**dict(row))

    async def get_languages(self, offset=0, limit=500) -> list[Language]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from languages order by name offset $1 limit $2', offset, limit)
        return [Language(**dict(r)) for r in rows]

    async def get_language(self, language_iso: str) -> Language | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from languages where iso_639_1=$1', language_iso)
        return Language(**dict(row)) if row else None

    async def upsert_language(self, language: Language) -> Language:
        if language.iso_639_1 is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into languages(name) VALUES ($1) returning *",
                                                language.name)
        elif await self.get_language(language.iso_639_1) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into languages(iso_639_1, name) VALUES ($1,$2) returning *",
                                                language.iso_639_1, language.name)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update languages set name=$2 where iso_639_1=$1 returning *""",
                                                language.iso_639_1, language.name)

        return Language(**dict(row))

    async def get_keywords(self, offset=0, limit=500) -> list[Keyword]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch('select * from keywords order by name offset $1 limit $2', offset, limit)
        return [Keyword(**dict(r)) for r in rows]

    async def get_keyword(self, keyword_id: int) -> Keyword | None:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow('select * from keywords where keyword_id=$1', keyword_id)
        return Keyword(**dict(row)) if row else None

    async def upsert_keyword(self, keyword: Keyword) -> Keyword:
        if keyword.keyword_id is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into keywords(name) VALUES ($1) returning *",
                                                keyword.name)
        elif await self.get_keyword(keyword.keyword_id) is None:
            # insert
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("insert into keywords(keyword_id, name) VALUES ($1,$2) returning *",
                                                keyword.keyword_id, keyword.name)
        else:
            # update
            async with self.pool.acquire() as connection:
                row = await connection.fetchrow("""update keywords set name=$2 where keyword_id=$1 returning *""",
                                                keyword.keyword_id, keyword.name)

        return Keyword(**dict(row))


async def main_():
    db = DbService()
    await db.initialize()
    # await db.upsert_movie(Movie(1, 'Karramba'))
    await db.upsert_language(Language("iso", "test"))
    await db.upsert_keyword(Keyword(420, "test"))

if __name__ == '__main__':
    run(main_())
