from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from db import utils as database_utils


async_engine = create_async_engine(
    url=database_utils.database_url(),
    echo=database_utils.database_echo(),
)

async_session = async_sessionmaker(
        engine=async_engine,
        expire_on_commit=False,
)
