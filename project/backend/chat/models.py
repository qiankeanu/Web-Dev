from django.db import models
from users.models import Profile

class Message(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sent_message')
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver_message')
    text=models.TextField()
    timestap=models.DateTimeField(auto_now_add=True)
    is_readed=models.BooleanField(default=False)

    class Meta:
        ordering=['-timestap']