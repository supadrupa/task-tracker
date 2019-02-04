from rest_framework.routers import SimpleRouter
from server.tasks.views import TaskViewSet

app_name = 'tasks'

router = SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
