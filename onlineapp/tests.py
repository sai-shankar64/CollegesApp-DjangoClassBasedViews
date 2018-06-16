from django.test import TestCase
from onlineapp.models import *
from onlineapp.serializers.model_serializers import *
# Create your tests here.
class AddCollegeTestCase(TestCase):
    def setUp(self):
        self.college=College.objects.create(name='vishnu', location= 'bvrm', acronym= 'VIT', contact= 'contact@vishnu.edu.in')
        self.serializer=CollegeSerializer(self.college)

    def test_add_college_valid_serializer(self):
        self.assertEqual(self.serializer.data,{'name': 'vishnu', 'location': 'bvrm', 'acronym': 'VIT', 'contact': 'contact@vishnu.edu.in'})

    def test_add_college_invalid_serializer(self):
        self.assertNotEqual(self.serializer.data,{'name': 'vishnu', 'location': 'bvrm', 'acronym': 'VIIT', 'contact': 'contact@vishnu.edu.in'})


class GetCollegeTestCase(TestCase):
    def setUp(self):
        # import ipdb
        # ipdb.set_trace()
        self.college = College.objects.create(name="SRKR College of engineering", location="Bhimavaram", acronym="srkr", contact="contact@srkr.edu")
        self.college=College.objects.get(name='SRKR College of engineering')
        self.serializer=CollegeSerializer(self.college)

    def test_get_college_valid_serializer(self):
        self.assertEqual(self.serializer.data,{"name": "SRKR College of engineering", "location": "Bhimavaram", "acronym": "srkr", "contact": "contact@srkr.edu"})

    def test_get_college_invalid_senrializer(self):
        self.assertNotEqual(self.serializer.data,
                         {"name": "SRKR College of engineering", "location": "Bhimavaram", "acronym": "srkrr",
                          "contact": "contact@srkr.edu"})