
from django.contrib import admin
from django.urls import path, include

from skills.views import SkillListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/skills/", include('skills.urls'), name='skills'),   
]
