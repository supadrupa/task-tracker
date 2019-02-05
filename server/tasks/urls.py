from rest_framework.routers import DefaultRouter

from server.tasks.views import TaskViewSet, ProjectViewSet, CommentViewSet


app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls
