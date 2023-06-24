from django.test import TestCase

# Create your tests here.


class TestDRFTestCase(TestCase):
    
    def test_get(self):
        
        output = self.client.get("/api/home/?a=11&b=8")
        
        print(output.status_code)
        
        self.assertEqual(output.json(),{"sum":11+8})