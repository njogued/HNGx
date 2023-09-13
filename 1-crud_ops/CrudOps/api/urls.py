from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_data, name='GET & POST'),
    path('', views.get_data, name='GET & POST'),
    path('api/<int:pk>', views.UserInfo.as_view(),
         name="Read, Update, Delete"),

    # If using username as lookup field use this path.
    # --> Also comment out lookup field in views.UserInfo
    # path('api/<str:name>/', views.UserInfo.as_view(),
    #      name="Read, Update, Delete"),
    # path('api', views.addPerson, name=['New Person POST']),
]
