from django.urls import path, include, re_path
from .views import TaskList, DetailView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, logout_user, \
RegisterPage
from django.contrib.auth.views import LogoutView

from .api_views import TaskListAPI, TaskDetailAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),


    path('api/tasks/', TaskListAPI.as_view(), name='api-task-list'),
    path('api/tasks/<int:pk>/', TaskDetailAPI.as_view(), name='api-task-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/tasks/auth', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

]