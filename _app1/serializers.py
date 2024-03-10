# from rest_framework import serializers
# from .models import Students

# class StudentSerializers(serializers.ModelSerializer):
#     class Meta:
#          model=Students
#          field= "__all__"

from rest_framework import serializers
from .models import Students

#this is student 
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
         model = Students
         fields = "__all__"
