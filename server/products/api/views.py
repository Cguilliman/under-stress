from .serializers import ProductSerializer, CreateProductSerializer
from products.models import Product
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status


class ProductCreateAPIView(CreateAPIView):
    serializer_class = CreateProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = None
        if request.user.is_authenticated:
            user = request.user

        product = Product.objects.create(author=user, **serializer.data)
        product_data = ProductSerializer(product).data

        headers = self.get_success_headers(product_data)
        return Response(product_data, status=status.HTTP_201_CREATED, headers=headers)


class ProductReceiveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        product = Product.objects.filter(id=self.kwargs.get("product_id")).first()
        if product is not None:
            return product
        raise NotFound()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
