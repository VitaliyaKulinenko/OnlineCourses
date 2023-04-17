from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from courses.models import Lection, Course, Hometask
from courses.permissions import IsOwnerOrReadOnly, Isteacher
from courses.serializers import LectionSerializer, CourseSerializer, HometaskSerializer


class LectionAPIList(ListAPIView):
    queryset = Lection.objects.all()
    serializer_class = LectionSerializer
    permission_classes = (IsAuthenticated,)


class LectionAPICreateList(CreateAPIView):
    queryset = Lection.objects.all()
    serializer_class = LectionSerializer
    permission_classes = (IsAuthenticated, Isteacher)


class LectionAPIDelete(RetrieveDestroyAPIView):
    queryset = Lection.objects.all()
    serializer_class = LectionSerializer
    permission_classes = (IsOwnerOrReadOnly, Isteacher)


class LectionAPIUpdate(viewsets.ModelViewSet):
    queryset = Lection.objects.all()
    serializer_class = LectionSerializer
    permission_classes = (IsOwnerOrReadOnly, Isteacher)


class CourseAPIList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, Isteacher)


class CourseAPICreateList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, Isteacher)


class HometaskAPIList(ListAPIView):
    queryset = Hometask.objects.all()
    serializer_class = HometaskSerializer
    permission_classes = (IsAuthenticated,)


class HometaskAPICreateList(CreateAPIView):
    queryset = Hometask.objects.all()
    serializer_class = HometaskSerializer
    permission_classes = (IsAuthenticated, Isteacher)


class HometaskAPIDelete(RetrieveDestroyAPIView):
    queryset = Hometask.objects.all()
    serializer_class = HometaskSerializer
    permission_classes = (IsOwnerOrReadOnly, Isteacher)


class HometaskAPIUpdate(viewsets.ModelViewSet):
    queryset = Hometask.objects.all()
    serializer_class = LectionSerializer
    permission_classes = (IsOwnerOrReadOnly, Isteacher)
