
from re import template
from django.contrib import admin
from django.urls import path,include
from tasks.urls import TaskRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('tasks.urls')),
    path('api/', include(TaskRouter.urls))
]
