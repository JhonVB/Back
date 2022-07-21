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
