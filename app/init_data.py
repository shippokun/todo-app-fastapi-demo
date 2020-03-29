# 初期データを流し込むためのスクリプト
# docker-compose run --rm app python init_data.py
from models import engine, db_session, Base, User, Task
Base.metadata.create_all(bind=engine)

taro = User(username='Taro')
db_session.add(taro)
hanako = User(username='Hanako')
db_session.add(hanako)

task1 = Task(
  user_id=taro.id,
  content='Task1',
)
db_session.add(task1)
task2 = Task(
  user_id=hanako.id,
  content='Task2',
)
db_session.add(task2)
db_session.commit()