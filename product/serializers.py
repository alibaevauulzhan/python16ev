from rest_framework import serializers

from product.models import Product, ProductReview


class ProductSerializer(serializers.ModelSerializer):
    """
    Класс который переводит данные в JSON формат
    """
    class Meta:
        model = Product
        exclude = ('created_at',)
        # exclude = ('created_at',)
        # fields = ('id', 'title', 'price', 'status', 'description')


class ProductCreateSerializer(serializers.ModelSerializer):
    """
  Класс который переводит данные в JSON формат
    """
    class Meta:
        model = Product
        fields = ('title', 'image', 'price', 'description')

class ProductReviewSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField("get_product_title")

    class Meta:
        model = ProductReview
        fields = "__all__"

    def get_product_title(self, product_review):
        title = product_review.product.title
        return title
    def validate_product(self, product):
        #
        if self.Meta.model.objects.filter(product=product).exists():
            raise serializers.ValidationError(
                "Вы уже оставляли отзыв на этот продукт"
            )
        return product

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating