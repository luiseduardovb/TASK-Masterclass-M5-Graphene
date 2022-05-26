class Query(FoodQuery,graphene.ObjectType):
    greet = graphene.String(name=graphene.String())

    def resolve_greet(root,info, name):
        return f'Hello {name}'


