from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls import include, url  # For django versions before 2.0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('questions.urls'))


]

# if settings.DEBUG:
#  import debug_toolbar
#  urlpatterns = [
#  path('__debug__/', include(debug_toolbar.urls)),
#  ] + urlpatterns
