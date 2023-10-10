from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, EventOrganizers , Customers ,TicketType
from .serializers import TicketTypeSerializer, CustomersSerializer ,EventOrganizersSerializer, EventSerializer , EventUserLoginSerializer
import jwt
from Event_booking_system.settings import SECRET_KEY
from datetime import datetime , timedelta
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from app.task import send_mail_func
from django.shortcuts import HttpResponse

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class CR(APIView):
    def post(self, request, format=None):
        serializer = EventOrganizersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        send_mail_func.delay()
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = EventUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')

        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)



def send_email_to_all(request):
    send_mail_func.delay()
    return HttpResponse("sent")