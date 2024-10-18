from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

#создание и просмотр записи(ей)
class TaskListAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    #сохраняет таску в профиль авторизованного в данный момент юзера
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#изменение определенных записей(пример)http://127.0.0.1:8000/api/tasks/1/
class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
