from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from django.db import transaction
from rest_framework import status
import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_user(request):
    print("==== REGISTER REQUEST DATA ====")
    print("request.data:", request.data)
    print("request.FILES:", request.FILES)
    print("==== LOGIN ATTEMPT DATA ====")
    print("Username/Email:", request.data.get('username'))
    print("Password present:", bool(request.data.get('password')))
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    profile_data = {
        'surname': request.data.get('profile.surname'),
        'middle_name': request.data.get('profile.middle_name'),
        'given_name': request.data.get('profile.given_name'),
        'birthday': request.data.get('profile.birthday'),
        'phone_number': request.data.get('profile.phone_number'),
        'status': request.data.get('profile.status'),
        'photo': request.FILES.get('profile.photo')
    }

    # Check for missing fields except photo
    missing = [k for k, v in profile_data.items() if k != 'photo' and not v]
    if not username or not email or not password or missing:
        return Response({'detail': f'Missing fields: {missing}'}, status=400)

    if not username or not email or not password:
        return Response({'detail': 'Please provide username, email and password'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'detail': 'Username already exists'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        return Response({'detail': 'Email already exists'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    try:
        with transaction.atomic():
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            # Create profile with additional data
            profile = Profile.objects.create(
                user=user,
                surname=profile_data.get('surname', ''),
                middle_name=profile_data.get('middle_name', ''),
                given_name=profile_data.get('given_name', ''),
                birthday=profile_data.get('birthday'),
                phone_number=profile_data.get('phone_number', ''),
                status=profile_data.get('status', 'AS')
            )

            # Handle photo if provided
            photo = request.FILES.get('profile.photo')
            if photo:
                profile.photo = photo
                profile.save()
            
        return Response({
            'detail': 'User registered successfully',
            'user_id': user.id
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error("Registration error: %s", str(e), exc_info=True)
        return Response({
            'detail': str(e),
            'request_data': request.data  # Include request data in error response
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
