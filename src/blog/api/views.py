from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Blog
from blog.api.serializers import BlogSerializer

# GET
@api_view(['GET', ])
def api_details_blog_view(req, id):

    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

# PUT
@api_view(['PUT', ])
def api_update_blog_view(req, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'PUT':
        serializer = BlogSerializer(blog, data=req.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = 'update Successfully'
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE
@api_view(['DELETE', ])
def api_delete_blog_view(req, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'DELETE':
        operation = blog.delete()
        data = {}
        if operation:
            data['success'] = 'Delete Successfull'
        else:
            data['failure'] = 'Delete failed'
        return Response(data=data)

# POST
@api_view(['POST', ])
def api_create_blog_view(req):
    if req.method == "POST":
        serializer = BlogSerializer(data=req.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)