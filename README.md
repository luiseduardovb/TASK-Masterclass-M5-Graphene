# Graphene

Wow, magic, amazing!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M5-Graphene).
   - The repository was set up using the steps [here](https://gist.github.com/malthunayan/0497ba9758cf9ddd7380c76f806adbe3).
2. Make sure to have `python 3.9.10` installed (use `pyenv install 3.9.10` to ensure it is installed).
3. Install the project dependencies using `poetry install`.
4. Run the migrations using `poetry run manage migrate`.

## Queries & Graphene Setup

1. Add `graphene_django` to your `INSTALLED_APP`.
2. Create a `Query` inside of `recipes/schemas.py`.
   - Inherit from `graphene.ObjectType` for now and just `pass`
3. Create a `SCHEMA` variable that will instantiate a `graphene.Schema` object.
   - Pass it your `Query` class.
4. Go to `recipes/urls.py` and add `GraphQLView` to your list of paths. Make sure to:
   - Name the endpoint `graphql/`
   - Enable `graphiql` based on `settings.DEBUG`.
   - Add your `SCHEMA` to the view.
5. Add a `greet` resolver to your query. It should accept a `name` and respond to that name with a greeting.

## Graphene-Django Queries

1. Create a `type` in `food/types.py` for all the models in `food/models.py` (make sure to inherit from `graphene_django.DjangoObjectType`).
2. Import all the types you have created in `food/types.py` into `schemas.py` (even if you do not end up using them), and to make things simpler import them using a wildcard (i.e., `from food.types import *`).
3. Create a `FoodQuery` in `food/schemas.py`, which will inherit from `graphene.ObjectType`.
4. Create a resolver for a single `recipe`, which will take in an ID.
5. Create a resolver for many `recipes`.
6. Import your `FoodQuery` into `recipes/schemas.py`, and let `Query` inherit from `FoodQuery` (it should be the class before `graphene.ObjectType`).
7. Create some objects using the shell, and check that your queries work on `Altair GraphQL Client`.

## Graphene-Django Queries Bonus

Add an optional limit clause to your `recipes` resolver. The resolver should default this parameter to `None`, and if it receives it, then it should limit the query.
