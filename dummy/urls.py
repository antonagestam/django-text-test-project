from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from text.urls import urlpatterns as django_text_patterns

from .views import uhn_tiss

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^django_text/', include(django_text_patterns, namespace='django_text')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^render/$', uhn_tiss, name='render'),
)
