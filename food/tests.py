import json
from functools import partial

import pytest
from django.test import Client
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client: Client) -> partial[graphql_query]:
    return partial(graphql_query, client=client)


@pytest.mark.task1
def test_greet(client_query: partial[graphql_query]) -> None:
    response = client_query(
        """
        query {
            greet(name: "Foo")
        }
        """
    )

    content = json.loads(response.content)
    assert "errors" not in content


@pytest.mark.task2
@pytest.mark.django_db
@pytest.mark.parametrize(
    "query",
    [
        """
        query {
            recipe(recipeId: 1) {
                id
                name
            }
        }
        """,
        """
        query {
            recipe(recipeId: 1) {
                id
                name
                steps
                ingredients {
                    id
                    name
                    origin
                }
                cuisine {
                    id
                    name
                }
            }
        }
        """,
    ],
)
def test_recipe(query: str, client_query: partial[graphql_query]) -> None:
    response = client_query(query)

    content = json.loads(response.content)
    assert "errors" not in content


@pytest.mark.django_db
@pytest.mark.parametrize(
    "query",
    [
        """
        query {
            recipes {
                id
                name
            }
        }
        """,
        """
        query {
            recipes {
                id
                name
                steps
                ingredients {
                    id
                    name
                    origin
                }
                cuisine {
                    id
                    name
                }
            }
        }
        """,
    ],
)
def test_recipes(query: str, client_query: partial[graphql_query]) -> None:
    response = client_query(query)

    content = json.loads(response.content)
    assert "errors" not in content


@pytest.mark.task3
@pytest.mark.django_db
def test_delete_recipe(client_query: partial[graphql_query]) -> None:

    response = client_query(
        f"""
        mutation {{
            deleteRecipe(id: 1) {{
                status
            }}
        }}
        """
    )

    content = json.loads(response.content)
    assert "errors" not in content

    assert not content["data"]["deleteRecipe"]["status"]
