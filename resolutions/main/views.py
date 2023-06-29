from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, UserManager

from .models import *
from .serializer import *

from django.http import HttpResponseRedirect, HttpRequest, HttpResponseForbidden, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getResa(request):
    r = Resolution.objects.all()
    serializer = ResolutionSerializer(r, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def format_options(request):
    formats = Format.objects.all()
    format_names = [format.name for format in formats]
    return Response(format_names)

@api_view(['GET'])
def category_options(request):
    categories = Category.objects.all()
    category_names = [category.name for category in categories]
    return Response(category_names)

@api_view(['POST'])
def create_resolution(request):
    serializer = ResolutionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_resolution(request, pk):
    resolution = get_object_or_404(Resolution, pk=pk)
    serializer = ResolutionSerializer(resolution)
    serializer.delete(resolution)
    return Response(status=204)
