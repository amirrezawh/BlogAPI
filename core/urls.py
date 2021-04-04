from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('Users.urls', 
    namespace="registeration")),

    path('api/v1/blog/', include('Blog.urls',
    namespace="blog")),
]
