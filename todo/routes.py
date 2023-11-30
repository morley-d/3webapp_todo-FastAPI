from fastapi import Request, Depends
from sqlalchemy.orm import Session

from config import settings
from database.base import get_db
from models import ToDo
from todo.main import app, templates


@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list':  todos})
