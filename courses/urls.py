from django.urls import path

from courses.views import CourseAPIList, CourseAPICreateList, LectionAPIList, LectionAPICreateList, LectionAPIUpdate, \
    LectionAPIDelete

urlpatterns = [

    path('course/', CourseAPIList.as_view()),
    path('course/create', CourseAPICreateList.as_view()),
    path('lection/', LectionAPIList.as_view()),
    path('lection/create/', LectionAPICreateList.as_view()),
    path('lection/update/<int:pk>/', LectionAPIUpdate.as_view({'get': 'list'})),
    path('lection/delete/<int:pk>/', LectionAPIDelete.as_view()),

]