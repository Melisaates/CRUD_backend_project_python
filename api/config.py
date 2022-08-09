from sqlalchemy import create_engine


class Config:
    connstr = "postgresql://postgres:postgresql@localhost:5432/Products"
    engine = create_engine(connstr, echo=True)
    conn = engine.connect()


settings = Config()
