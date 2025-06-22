
# local files
from db.connection import BaseModel, Base,engine

Base.metadata.create_all(engine)


