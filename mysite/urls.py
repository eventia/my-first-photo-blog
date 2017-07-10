from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from blog.views import post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)
