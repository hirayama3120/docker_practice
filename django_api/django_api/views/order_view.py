import json
from rest_framework import status, views
from rest_framework.response import Response

from django_api.serializers.order_serializer import OrderSerializer
from django_api.repositories.order_repository import OrderRepository

class OrderView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        record = OrderRepository().register(serializer.validated_data)

        return Response(
            {
                "id": record.id
            },
            status=status.HTTP_200_OK)
