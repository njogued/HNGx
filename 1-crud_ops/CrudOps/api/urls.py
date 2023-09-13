from django.urls import path
from . import views

urlpatterns = [
    path('api', views.get_data, name='GET & POST'),
    path('', views.get_data, name='GET & POST'),
    path('api/<str:name>', views.UserInfo.as_view(),
         name="Read, Update, Delete"),
    # path('api', views.addPerson, name=['New Person POST']),
]
