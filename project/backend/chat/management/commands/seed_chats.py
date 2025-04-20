from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile
from chat.models import Message
from faker import Faker
import random
fake= Faker()
class Command(BaseCommand):
    help=" Seeding database to make fake messages for testing"
    def handle(self, *args, **options):
        profiles=list(Profile.objects.all())

        if len(profiles)<2:
            self.stdout.write(self.style.ERROR("❌ not enough profiles"))
            return 
        message_count=0
        for i in range(50):
            sender,receiver=random.sample(profiles,2)

            Message.objects.get_or_create(
                sender=sender,
                receiver=receiver,
                text=fake.sentence(nb_words=random.randint(10,30)),
                is_readed=random.choice([True,False])
            )
            message_count+=1
        self.stdout.write(self.style.SUCCESS(f"✅ succesfully created {message_count} messages"))
    
