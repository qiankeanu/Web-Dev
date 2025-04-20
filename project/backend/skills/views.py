from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Skills,UserSkills
from users.models import Profile
from .serializers import SkillSerializer,UserSkillSerializer

class SkillView(viewsets.ModelViewSet):
    queryset=Skills.objects.all()
    serializer_class=SkillSerializer

class UserSkillView(viewsets.ModelViewSet):
    queryset=UserSkills.objects.all()
    serializer_class=UserSkillSerializer

@api_view(['GET'])
def get_userSkills(request,id):
    profile=get_object_or_404(Profile,id=id)
    user_skills=UserSkills.objects.filter(user=profile)
    serializer=UserSkillSerializer(user_skills,many=True)
    return Response(serializer.data)