from django.db import models
from users.models import Profile
class KnowledgeLevel(models.TextChoices):
    ELEMENTARY="E","Elementary level or juniour level"
    Beginner="B","Basic level or juniour plus level"
    Average="A","Average level or middle level"
    Indermediate="I","Advanced knowledge or middle plus level"
    UpperIndermediate="U","Mastered knowledge of basic and some advanced knowledge or seniour minus level"
    Complex="C","Complex knowledge or seniour level"
    Proficient="P","Mastered everything in specific knowledge or seniour plus level"


class Skills(models.Model):
    name=models.CharField(max_length=255,unique=True)
    category=models.CharField(max_length=255)
    knowledge_level=models.CharField(choices=KnowledgeLevel.choices,max_length=1)
    description=models.TextField()
    def __str__(self):
        return self.name
class UserSkills(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="users_skilled")
    skill=models.ForeignKey(Skills,on_delete=models.CASCADE,related_name="users_with_skill")
    level=models.CharField(choices=KnowledgeLevel.choices,max_length=1,verbose_name="specific_knowlegde")
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.skill.name} ({self.get_level_display()})"
    class Meta:
        unique_together=('user','skill')