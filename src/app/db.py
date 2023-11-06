from app.config import DATABASE_URL

from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData)
from databases import Database
from datetime import datetime as dt
from pytz import timezone as tz

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("completed",String(8), default="False"),
    Column("created_date", String(50), default=dt.now(tz("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M"))
)
# Databases query builder

database = Database(DATABASE_URL)
