from django.conf.urls.defaults import url, patterns, include

from views import HomepageView, OrderListView

urlpatterns = (
    url(r'^', HomepageView.as_view(), name='url_homepage'),
    url(r'^order/$', OrderListView.as_view(), name='url_orders'),
)
