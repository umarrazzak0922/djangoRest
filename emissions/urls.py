from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('imdex', views.index, name='index'),
    re_path(r'^reports/(?P<year>[0-9]{4})/$',
            views.emissionreport,
            name='reports'),
    re_path(r'^search/reports/(?P<year>[0-9]{4})/$',
            views.searchemissionreport,
            name='search_reports'),
    path('upload/form',
         views.renderEmissionFileUploadPage,
         name='emission_file_upload_form'),
    path('upload-emission',
         views.uploadEmissionFile,
         name='emission_file_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
