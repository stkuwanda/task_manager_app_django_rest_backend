from tasks.models import Task
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from tasks.serializers import TaskSerializer, UserSerializer


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# This is also another way of achieving the same outcome using APIView but ModelViewSets are much simpler.

# from models import Task
# from serializers import TaskSerializer
# from rest_framework.views import APIView, View
# from rest_framework.permissions import IsAuthenticated
# from django.http import Http404
# from rest_framework.response import Response
# from rest_framework import status

# class TaskViewSet(APIView):
#     """
#     List or create new tasks
#     """
#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk, user):
#         try:
#             # This filter makes sure that the user owns the task with that primary key.
#             return Task.objects.filter(owner=user).get(pk=pk)
#         except Task.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         if pk:
#             task = self.get_object(pk=pk, user=request.user)
#             serializer = TaskSerializer(task)
#             return Response(serializer.data)
#         else:
#             tasks = Task.objects.filter(owner=request.user)
#             serializer = TaskSerializer(tasks, many=True)
#             return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         task = self.get_object(pk=pk, user=request.user)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         task = self.get_object(pk=pk, user=request.user)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
