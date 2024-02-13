from django.contrib import admin
from django.urls import path, include
admin.site.site_header="Hack-Store"
admin.site.site_title ="Admin Hack-Store"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
