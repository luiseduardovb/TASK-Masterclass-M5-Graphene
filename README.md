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
   - `csrf_exempt` the view.
5. Add a `greet` resolver to your query. It should accept a `name` and respond to that name with a greeting.

## Graphene-Django Queries

1. Create a `type` in `food/types.py` for all the models in `food/models.py` (make sure to inherit from `graphene_django.DjangoObjectType`).
2. Create a `FoodQuery` in `food/schemas.py`, which will inherit from `graphene.ObjectType`.
3. Create a resolver for a single `recipe`, which will take in a `recipe_id` (hint: `recipe` will be a `graphene.Field` type).
4. Create a resolver for many `recipes` (hint: use `graphene_django.DjangoListField` to simplify things).
5. Import your `FoodQuery` into `recipes/schemas.py`, and let `Query` inherit from `FoodQuery` (it should be the class before `graphene.ObjectType`).
6. Create some objects using the admin panel, and check that your queries work on `Altair GraphQL Client`.

## Graphene-Django Queries Bonus

Add an optional limit clause to your `recipes` resolver. The resolver should default this parameter to `None`, and if it receives it, then it should limit the query.

## Mutations

1. Add a `Mutation` class that inherits from `graphene.ObjectType` in `recipes/schemas.py`, and just `pass`es for now.
2. Add your `Mutation` class to the `SCHEMA` variable in the same file (you should add it to the `graphene.Schema` constructor).
3. Add a `FoodMutation` in `foods/schemas.py` under your `FoodQuery` class, which inherits from `graphene.ObjectType`. This will be the container class for all your `food` mutations, for now it should just `pass`.
4. Import your `FoodMutation` into `recipes/schemas.py`, and let `Mutation` inherit from `FoodMutation` (it should be the class before `graphene.ObjectType`).
5. Add a `DeleteRecipe` mutation class (should inherit from `graphene.Mutation`), it should take in a `recipe_id` as an argument (it should be an integer).
6. Add a return type under your `arguments`, which will just be a `graphene.Boolean` variable named `status`.
7. In the `mutate` method you should try to `get` the `recipe` object with that `id`, and `delete` it.
   - If you found the object and deleted it, return a `DeleteRecipe` instance with `status=True`.
   - If you have not found the object, return a `DeleteRecipe` instance with `status=False`.
8. Add this mutation to your `FoodMutation` class, by removing `pass` and adding a variable called `delete_recipe` which is equal to `DeleteRecipe.Field()`.
9. Test that your mutation works on `Altair GraphQL Client`.
