from pydantic import BaseModel

class VideoGame(BaseModel):
    id: int
    title: str
    developer: str
    publisher: str
    year_published: int
    sales: int

class User(BaseModel):
    username: str
    token: str
    is_admin: bool
    email: str
