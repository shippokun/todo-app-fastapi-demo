import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import User as UserModel, Task as TaskModel

class User(SQLAlchemyObjectType):
  class Meta:
    # TODO: ここの仕様を調べる
    model = UserModel
    interfaces = (relay.Node, )


class UserConnections(relay.Connection):
  class Meta:
    node = User


class Task(SQLAlchemyObjectType):
  class Meta:
    model = TaskModel
    interfaces = (relay.Node, )


class TaskConnections(relay.Connection):
  class Meta:
    node = Task


class Query(graphene.ObjectType):
  node = relay.Node.Field()
  # デフォルトではソートが有効化されている
  all_users = SQLAlchemyConnectionField(UserConnections)
  # ソートを無効化
  all_tasks = SQLAlchemyConnectionField(TaskConnections, sort=None)


schema = graphene.Schema(query=Query)