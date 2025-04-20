from rest_framework import serializers
from .models import Skills,UserSkills

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields='__all__'

class UserSkillSerializer(serializers.ModelSerializer):
    skills=SkillSerializer()
    class Meta:
        model=UserSkills
        fields=['skills','level']