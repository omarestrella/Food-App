from django.conf.urls.defaults import patterns, include, url

from views import HomepageView

urlpatterns = (
    url(r'^$', HomepageView.as_view(), name='url_homepage'),
)
