from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Person
from .serializers import PersonSerializer
from rest_framework import generics


@api_view(['GET', 'POST'])
def get_data(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()


@api_view(['GET', 'PUT', 'DELETE'])
def rud_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


class UserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'
