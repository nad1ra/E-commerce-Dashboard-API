from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
                  'name',
                  'description',
                  'parent',
                  'image',
                  'created_at',
                  'updated_at'
        ]

class CategoryDetailSerializer(CategorySerializer):

    class Meta(CategorySerializer.Meta):
        fields = super().fields + ['parent_name', 'product_info']

    def get_parent_name(self, obj):
        return obj.parent.name

    def get_product_info(self, instance):
        return {
            'count': instance.products.count(),
            'products': ProductCategorySerializer(instance.products).data
        }


'''class CategoryDetailSerializer(serializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    parent = serializers.IntegerField(read_only=True)
    parent_name = serializers.SerializerMethodField()
    image = serializers.ImageField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    '''