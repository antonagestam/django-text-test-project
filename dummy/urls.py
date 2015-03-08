from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from text.urls import urlpatterns as django_text_patterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dummy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^django_text/', include(django_text_patterns, namespace='django_text')),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
)
