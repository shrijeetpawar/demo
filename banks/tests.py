from django.test import TestCase
from graphene.test import Client
from banks.schema import schema
from banks.models import Bank, Branch
from django.db import connection


class GraphQLBranchQueryTest(TestCase):
    databases = '__all__'

    @classmethod
    def setUpTestData(cls):
        # Create tables manually for unmanaged models
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Bank)
            schema_editor.create_model(Branch)

        bank = Bank.objects.create(id=123, name="Test Bank")
        Branch.objects.create(
            ifsc="TEST0001",
            bank=bank,
            branch="Main Branch",
            address="123 Test Street",
            city="Test City",
            district="Test District",
            state="Test State"
        )

    def test_graphql_branch_query(self):
        client = Client(schema)
        query = '''
        query {
          branches {
            ifsc
            branch
            bank {
              name
            }
          }
        }
        '''
        result = client.execute(query)
        self.assertEqual(result["data"]["branches"][0]["branch"], "Main Branch")
