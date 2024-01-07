from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import generics

#API views
# class bookingview(APIView):
#     def get (self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)
#     def post (self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

# ModelViewset per course instructions
class bookingview(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class menuview(APIView):
    def get (self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

class singlemenuitemview(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
