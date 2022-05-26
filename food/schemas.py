import graphene
import graphene_django
from graphql import GraphQLError

from food.models import Ingredient, Recipe
from food.types import IngredientType, RecipeType



class FoodQuery(graphene.ObjectType):
    recipe = graphene.Field(RecipeType, recipe_id=graphene.Int())
    # recipes = graphene.List(RecipeType)
    recipes = graphene_django.DjangoListField(RecipeType, limit=graphene.Int())

    def resolve_recipe(root,info, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            return recipe
        except Recipe.DoesNotExist:
            return None

    
    def resolve_recipes(root,info,limit=None):
        queryset = Recipe.objects.all()
        if limit != None:
            return queryset[:limit]
        else:
            return  queryset

class DeleteRecipeMutation(graphene.Mutation):
    status = graphene.Boolean()
    class Arguments:
        recipe_id = graphene.Int()
    
    recipe = graphene.Field(RecipeType)

    def mutate(root, info, recipe_id):
        
        try:
            recipe_instance = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            return DeleteRecipeMutation(status=False)
        
        recipe_instance.delete()
        return DeleteRecipeMutation(status=True)


class UpdateIngredientMutation(graphene.Mutation):

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        origin = graphene.String()

    ingredient = graphene.Field(IngredientType)

    def mutate(root, info, **kwargs):
        try:
            ingredient_instance = Ingredient.objects.get(pk=kwargs.pop('id'))
        except Ingredient.DoesNotExist:
            raise GraphQLError("Ingredient does not exist")
        
        for attr,val in kwargs.items():
            setattr(ingredient_instance,attr,val)
        
        ingredient_instance.save()

        return UpdateIngredientMutation(ingredient=ingredient_instance)
        
        



class FoodMutation(graphene.ObjectType):
    delete_recipe = DeleteRecipeMutation.Field()
    update_ingredient = UpdateIngredientMutation.Field()



