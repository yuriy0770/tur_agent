from rest_framework.generics import ListAPIView

from api.serializers import CategorySerializers
from main.models import Category


class CategoryApi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers