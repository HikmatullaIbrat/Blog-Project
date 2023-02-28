from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import HttpResponse
from .models import BlogPost
from rest_framework.decorators import api_view, permission_classes
from .serializers import BlogPostSerializer,BlogPracticeSerializer

@api_view()
@permission_classes((permissions.AllowAny,))
def blog_list(request):
    # return Response('successfull attempt')
    allBlogs= BlogPost.objects.all()
    serializer = BlogPracticeSerializer(allBlogs, many=True)
    return Response(serializer.data)

@api_view()
@permission_classes((permissions.AllowAny,))
def blog_id_view(request, id):
    # return Response(id)
    # try:
    #     blog_number = BlogPost.objects.get(pk=id)
    #     serializer  = BlogPracticeSerializer(blog_number)
    #     return Response(serializer.data)
    # except BlogPost.DoesNotExist:
    #     return Response(status=404)
    # instead of all above code we can write
    blog_number = get_object_or_404(BlogPost, pk=id)
    serializer = BlogPracticeSerializer(blog_number)
    return Response(serializer.data)


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = BlogPostSerializer(queryset, many=True)
        
        return Response(serializer.data)
