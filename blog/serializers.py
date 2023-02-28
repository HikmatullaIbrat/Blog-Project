from rest_framework import serializers
from .models import BlogPost
# Serializer defines the API representation
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        lookup_field = 'slug'

class BlogPracticeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    contents_blog = serializers.CharField(max_length=255, source="content")
    datePublished = serializers.SerializerMethodField(method_name="calculate_date")

    # it is a custome serielizer field which is not existed in model of Blog
    def calculate_date(self, date_of:BlogPost):
        return date_of.date_created
