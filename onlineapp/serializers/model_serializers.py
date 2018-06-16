from rest_framework import serializers
from onlineapp.models import *
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer

class CollegeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    location = serializers.CharField(max_length=64)
    acronym = serializers.CharField(max_length=10)
    contact = serializers.EmailField(max_length=50)

    def create(self,validated_data):
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance

class MockTest1Serializer(serializers.ModelSerializer):
    class Meta:
        model=MockTest1
        fields=('id','problem1','problem2','problem3','problem4','total','student')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'dob', 'email', 'db_folder', 'dropped_out', 'college','mocktest1')


class StudentDetailsSerializer(serializers.ModelSerializer):
    mocktest1 = MockTest1Serializer()
    class Meta:
        model=Student
        fields = ('id', 'name', 'dob', 'email', 'db_folder', 'dropped_out','mocktest1')
    def create(self,validated_data):
        import ipdb
        ipdb.set_trace()
        return Student.objects.create(**validated_data)

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=128)
#     dob = serializers.DateField(allow_null=True)
#     email = serializers.EmailField(max_length=50)
#     db_folder = serializers.CharField(max_length=50)
#     dropped_out = serializers.BooleanField(default=False)
#     college=serializers.RelatedField(source='College',read_only=True)
#
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)
#
#
# class MockTest1Serializer(serializers.Serializer):
#     problem1 = serializers.IntegerField()
#     problem2 = serializers.IntegerField()
#     problem3 = serializers.IntegerField()
#     problem4 = serializers.IntegerField()
#     total = serializers.IntegerField()
#     # student = serializers.RelatedField(source='Student', read_only=True)
#
#     def create(self,validated_data):
#         return MockTest1.objects.create(**validated_data)
#
#
# class StudentAndMarksSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=128)
#     dob = serializers.DateField(allow_null=True)
#     email = serializers.EmailField(max_length=50)
#     db_folder = serializers.CharField(max_length=50)
#     dropped_out = serializers.BooleanField(default=False)
#     college=serializers.RelatedField(source='College',read_only=True)
#     mocktest1 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)



# def StudentTest(actual_output):
#     expected_output={'name': 'Vishnu institute of technology', 'location': 'Bhimavaram', 'acronym': 'vit', 'contact': 'contact@vit.edu'}
#     if not actual_output == expected_output:
#         raise AssertionError

# if __name__== "__main__":
#     # college = College(name='vishnu', location='bvrm', acronym='VIT', contact='contact@vishnu.edu.in')
#     college=College.objects.get(acronym='VIT')
#     college_serializer=CollegeSerializer(college)
#     json=JSONRenderer().render(college_serializer.data)
#
#     # StudentTest(college_serializer.data)
#     print(college_serializer.data)
#
#     stream=BytesIO(json)
#     data=JSONParser().parse(stream)
#     serializer=CollegeSerializer(data=data)
#     serializer.is_valid()
#     colg=serializer.save()


