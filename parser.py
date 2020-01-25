import requests
from sqlalchemy import MetaData, create_engine, declarative_base, Integer, BigInteger

engine = create_engine("'sqlite:///app.db", echo=True)
metadata = MetaData(bind=engine)
Base = declarative_base()

coords = Table(
    "coordiantes", metadata,
     Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
     Column("lang", BigInteger())
)

url = "https://mygeodata.cloud/data/cs2cs"
