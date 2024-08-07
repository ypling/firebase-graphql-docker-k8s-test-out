# models/todos.py
from sqlalchemy import Column, Integer, Boolean, Text, TIMESTAMP
from sqlalchemy.sql import func
from .db import Base, SCHEMA

class Todo(Base):
    __tablename__ = 'todos'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    done = Column(Boolean, nullable=False, default=False)
    task = Column(Text, nullable=False)
    due = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=True)

    def __repr__(self):
        return f"<Todo(id={self.id}, task='{self.task}', done={self.done}, due={self.due})>"