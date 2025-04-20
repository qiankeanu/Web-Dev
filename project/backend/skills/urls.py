from rest_framework.routers import DefaultRouter
from .views import SkillView,UserSkillView
from django.urls import path
from .views import get_userSkills

router =DefaultRouter()
router.register(r'skills',SkillView,basename='skills')
router.register(r'user-skills',UserSkillView,basename='user-skills')

urlpatterns=[
    path('user-skills/<int:id>/',get_userSkills,name='getuserskillsd')
]+router.urls