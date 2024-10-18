# api/v1/views/account_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from account.models import Account, UserProfile
from ..serializers import AccountSerializer, UserProfileSerializer

@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def account_detail(request, pk):
    account = cache.get(f'account_{pk}')
    if not account:
        account = get_object_or_404(Account, pk=pk)
        cache.set(f'account_{pk}', account, timeout=60*15)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@api_view(['GET'])
def account_list(request):
    accounts = cache.get('account_list')
    if not accounts:
        accounts = Account.objects.all()
        cache.set('account_list', accounts, timeout=60*15)
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'account_{pk}')
        cache.delete('account_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    cache.delete(f'account_{pk}')
    cache.delete('account_list')
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_user_profile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile_detail(request, pk):
    user_profile = cache.get(f'user_profile_{pk}')
    if not user_profile:
        user_profile = get_object_or_404(UserProfile, pk=pk)
        cache.set(f'user_profile_{pk}', user_profile, timeout=60*15)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['GET'])
def user_profile_list(request):
    user_profiles = cache.get('user_profile_list')
    if not user_profiles:
        user_profiles = UserProfile.objects.all()
        cache.set('user_profile_list', user_profiles, timeout=60*15)
    serializer = UserProfileSerializer(user_profiles, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user_profile(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    serializer = UserProfileSerializer(user_profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'user_profile_{pk}')
        cache.delete('user_profile_list')
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user_profile(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    user_profile.delete()
    cache.delete(f'user_profile_{pk}')
    cache.delete('user_profile_list')
    return Response(status=status.HTTP_204_NO_CONTENT)