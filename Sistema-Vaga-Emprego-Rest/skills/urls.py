from rest_framework import routers
from skills.views import SkillViewSet

app_name = 'skills'
router = routers.SimpleRouter()
router.register(r"", SkillViewSet, basename="skill")

urlpatterns = router.urls
