import re
from skills.models import Skills

def clean_text(text):
    # Remove punctuation & special characters
    return re.sub(r'[^\w\s]', '', text.lower())

def extract_skills_from_resume(resume_text):
    resume_text = clean_text(resume_text)
    tokens = resume_text.split()

    db_skills = [skill.name.lower() for skill in Skills.objects.all()]
    found_skills = set()

    for word in tokens:
        if word in db_skills:
            found_skills.add(word)

    return list(found_skills)
