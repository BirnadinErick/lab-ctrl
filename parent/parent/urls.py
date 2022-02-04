# Imports
from django.urls import path, include
from rest_framework import routers
from api import views

# BEGIN

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# END

if __name__ == '__main__':
    pass