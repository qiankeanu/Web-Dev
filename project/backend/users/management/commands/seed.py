from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile,Status
from skills.models import Skills,UserSkills,KnowledgeLevel
from phonenumber_field.phonenumber import PhoneNumber
import random
from datetime import date
from faker import Faker

fake=Faker()

class Command(BaseCommand):
    help="Seed database with users and profile with random skill and knowledge level"
    def handle(self, *args, **options):
        self.stdout.write("Seeding 🌱 ......")
        
        for i in range(20):
            username=f"user{i}"
            email=f"user{i}@test.com"

            user,created=User.objects.get_or_create(
                username=username,
                defaults={"email":email}
            )
            if created:
                user.set_password("12345678")
                user.save()
            
            profile,_=Profile.objects.get_or_create(
                user=user,
                defaults={
                    "surname":fake.last_name(),
                    "middle_name":fake.first_name(),
                    "given_name":fake.first_name_male(),
                    "birthday":fake.date_of_birth(minimum_age=18,maximum_age=55),
                    "phone_number":PhoneNumber.from_string(phone_number=fake.phone_number(), region="KZ"),
                    "status":random.choice(Status.values),
                }
            )

            all_skills=list(Skills.objects.all())
            sample_skills=random.sample(all_skills,k=5)
            for skill in sample_skills:
                UserSkills.objects.get_or_create(
                    user=profile,
                    skill=skill,
                    defaults={
                        "level":random.choice(KnowledgeLevel.values)

                    }
                )
        self.stdout.write(self.style.SUCCESS("✅ Seeded 20 users with profile and skills!"))
