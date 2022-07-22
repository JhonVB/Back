<<<<<<< HEAD
from django.urls import path
from tasks.views import PersonasViewset, getRoutes, MyTokenObtainPairView
from rest_framework import routers

from rest_framework_simplejwt.views import (
   TokenRefreshView
)

TaskRouter = routers.DefaultRouter()
TaskRouter.register(r'person', PersonasViewset)


urlpatterns =[
   path("",getRoutes),
   path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh')
]

=======
from django.urls import URLPattern, path
from tasks.views import PersonasViewset
from rest_framework import routers
TaskRouter = routers.DefaultRouter()
TaskRouter.register(r'person', PersonasViewset)

# funciones
# urlpatterns = [
#     path('persona/',persona_api_view,name="usuario_api"),
#     path('persona/<int:pk>/',persona_detail_api_view, name="usuario_detail_api_view" )
# ]

# CON CLASES
# urlpatterns = [
#     path('persona/',PersonasViewset.as_view(),name="Persona_api")
# ]
>>>>>>> 311a2a502f7fe1b8b72a7a081fcf49d64aebb43d
