
import graphene

from food.schemas import FoodMutation, FoodQuery
from food.models import Recipe


class Query(FoodQuery,graphene.ObjectType):
    greet = graphene.String(name=graphene.String())

    def resolve_greet(root,info, name):
        return f'Hello {name}'




class Mutation(FoodMutation, graphene.ObjectType):
    pass

SCHEMA = graphene.Schema(query=Query, mutation=Mutation)