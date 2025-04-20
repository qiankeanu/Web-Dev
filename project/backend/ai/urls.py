from django.urls import path
from . import views

urlpatterns=[
    path('parse-resume/',views.parse_resume,name='parse-resume'),
    path('greeting/',views.greeting,name='greeting'),
    path('match-profiles/<int:id>/',views.matching_profiles,name='match-profiles'),
    path('parse_resume_file/',views.parse_resume_file,name='parse_resume_file')
]