from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school_management.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls') ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
   
  #  config admin tittles  
  
admin.site.site_header = "Chakadini Admin Page"
admin.site.site_title = "Chakadini tittle"
admin.site.index_title= "welcome to chakadini admin page "