# from django.test import TestCase
from graphene_django.utils import GraphQLTestCase

# Create your tests here.

class GraphQLUserTest(GraphQLTestCase):
    # folder fixtures variable to the test class
    fixtures = ['users.json']
    def test_retrive_by_id(self):
        # jason data
        expected={
            "data":{
                "user":{
                    "id":"2",
                    "name": "saugat",
                    "followers": [
                        {
                            "name": "Avin Gyawli"
                        }
                    ]
                }
            }
        }

        res = self.query("""{
            user(id: 2){
                id
                name
                followers {
                    name
                }
            }
        }""")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(expected, res.json())
