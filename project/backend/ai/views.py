from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Profile
from skills.models import Skills,UserSkills
from ai.skill_extraction import extract_skills_from_resume
from ai.matchin import find_matching_profiles
from ai.file_parser import extract_text_from_docx,extract_text_PDF
from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def parse_resume(request):
    profile_id=request.data.get('profile_id')
    resume=request.data.get('resume_text')
    found=extract_skills_from_resume(resume)
    profile=Profile.objects.get(id=profile_id)
    skills_obj=Skills.objects.filter(name__in=found)

    for skill in skills_obj:
        UserSkills.objects.get_or_create(
            user=profile,
            skill=skill,
            defaults={'level':'B'}

        )
    return Response({'skills': [s.name for s in skills_obj]})
@api_view(['GET'])
def greeting(request):
    return Response({"message":"Hello?"})
@api_view(['GET'])
def matching_profiles(request,id):
    request.user
    try:
        matches=find_matching_profiles(id)
        return Response({'matches':matches})
    except Profile.DoesNotExist:
        return Response({'error':'Profile Not Found'},status=404)

@api_view(['POST'])
def parse_resume_file(request):
    request.user
    id=request.data.get('profile_id')
    file: UploadedFile=request.FILES.get('resume_file')
    file_type=file.name.split('.')[-1]
    
    if file_type=='pdf':
        resume_text=extract_text_PDF(file)
    elif file_type in ['doc','docx']:
        resume_text=extract_text_from_docx(file)
    else:
        return Response({'error':'UNsuppported typr'},status=404)
    
    found=extract_skills_from_resume(resume_text)
    profile=get_object_or_404(Profile,id=id)
    skills_obj=Skills.objects.filter(name__in=found)

    for skill in skills_obj:
        UserSkills.objects.get_or_create(user=profile,skill=skill,defaults={'level':'B'})
    return Response({'skills': [s.name  for s in skills_obj]})