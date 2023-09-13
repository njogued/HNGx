from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Person
from .serializers import PersonSerializer


@api_view(['GET'])
def get_data(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)
