from django.urls import path

from courses.views import CourseAPIList, CourseAPICreateList, LectionAPIList, LectionAPICreateList, LectionAPIUpdate, \
    LectionAPIDelete, HometaskAPIList, HometaskAPICreateList, HometaskAPIUpdate, HometaskAPIDelete

urlpatterns = [

    path('course/', CourseAPIList.as_view()),
    path('course/create', CourseAPICreateList.as_view()),
    path('lection/', LectionAPIList.as_view()),
    path('lection/create/', LectionAPICreateList.as_view()),
    path('lection/update/<int:pk>/', LectionAPIUpdate.as_view({'get': 'list'})),
    path('lection/delete/<int:pk>/', LectionAPIDelete.as_view()),
    path('hometask/', HometaskAPIList.as_view()),
    path('hometask/create/', HometaskAPICreateList.as_view()),
    path('hometask/update/<int:pk>/', HometaskAPIUpdate.as_view({'get': 'list'})),
    path('hometask/delete/<int:pk>/', HometaskAPIDelete.as_view()),

]