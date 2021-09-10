from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import CRUDApi
from .serializers import CRUDApiSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    # GET list of students, POST a new student, DELETE all students
    if request.methods == 'GET':
        students = CRUDApi.objects.all()
        name = request.GET.get('name', None)

        # if get none on parameter name then get all data student
        # to search student by name
        if name is not None:
            student = students.filter(name__icontains=name)

            student_serializer = CRUDApiSerializer(student, many=True)
            return JsonResponse(student_serializer.data, safe=False)
        else:
            students_serializer = CRUDApiSerializer(student, many=True)
            return JsonResponse(students_serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = CRUDApiSerializer(data=student_data)

        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # DELETE METHOD all student
        students = CRUDApi.objects.all()
        students.delete()
        return JsonResponse({'message': 'Students were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    # find student by id or pk
    try:
        student = CRUDApi.objects.get(pk=pk)
    except CRUDApi.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        student_serializer = CRUDApiSerializer(student)
        return JsonResponse(student_serializer.data)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student_serializer = CRUDApiSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        student.delete()
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def student_gender(request):
    # GET all published students
    students = CRUDApi.objects.filter(gender=True)

    if request.method == 'GET':
        students_serializer = CRUDApiSerializer(student, many=True)
        return JsonResponse(students_serializer.data, safe=False)