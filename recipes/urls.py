from django.urls import path
from django.contrib import admin

from calculator.views import omlet, pasta, buter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('omlet/<int:servings>', omlet),
    path('pasta/<int:servings>', pasta),
    path('buter/<int:servings>', buter),
]
