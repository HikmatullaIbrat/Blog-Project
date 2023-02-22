from rest_framework import serializers
from .models import BlogPost
# Serializer defines the API representation
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        lookup_field = 'slug'
