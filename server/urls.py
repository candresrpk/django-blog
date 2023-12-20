from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('blog/', include('blog.urls'), name='blog')
]
