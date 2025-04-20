from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,permissions
from .models import Message
from .serializer import MessageSerializer
from users.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import models

class MessageViewSet(viewsets.ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=400)
        serializer.save(sender=profile)
        return super().perform_create(serializer)
    
    @action(detail=False,methods=['get'],url_path='conversation/(?P<user_id>[^/.]+)')
    def conservation(self,request,user_id=None):
        me=self.request.user.profile
        other=get_object_or_404(Profile,id=user_id)
        message=Message.objects.filter(
            (models.Q(sender=me,receiver=other)| models.Q(sender=other,receiver=me))
        ).order_by('timestap')
        serializer=self.get_serializer(message,many=True)
        return Response(serializer.data)