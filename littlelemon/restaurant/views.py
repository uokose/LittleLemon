from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


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
class bookingview(viewsets.ModelViewSet): #Viewsets based views are registered using Router class
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class menuview(APIView):
    def get (self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

class singlemenuitemview(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # List of permission classes
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAdminUser]

    # For Function bases views, use decorator
    # @permission_classes([IsAuthenticated])
