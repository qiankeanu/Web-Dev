from skills.models import UserSkills
from users.models import Profile
from django.shortcuts import get_object_or_404

def find_matching_profiles(id):
    current_user=get_object_or_404(Profile,id=id)
    current_user_skills=set(UserSkills.objects.filter(user=current_user).values_list('skill_id',flat=True))
    matched_profiles=[]

    for profile in Profile.objects.exclude(id=id):
        profile_skills=set(UserSkills.objects.filter(user=profile).values_list('skill_id',flat=True))
        common_skills=current_user_skills & profile_skills

        if common_skills:
            matched_profiles.append({
                'id':profile.id,
                'full_name': profile.get_full_name(),
                'common_skills_count':len(common_skills),
            })
    matched_profiles.sort(key=lambda x:x['common_skills_count'],reverse=True)
    return matched_profiles