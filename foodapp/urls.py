from django.conf.urls.defaults import url, patterns, include

from views import HomepageView, OrderListView, UserOrderView, TodaysOrdersView

urlpatterns = (
    url(r'^$', HomepageView.as_view(), name='url_homepage'),
    url(r'^orders/$', OrderListView.as_view(), name='url_orders'),
    url(r'^orders/user/(?P<username>\w+)/$', UserOrderView.as_view(), name='url_user_orders'),
    url(r'^orders/today/$', TodaysOrdersView.as_view(), name='url_todays_orders'),
    #url(r'^orders/items/(?P<pk>\d+)/$', view, name='url_item_orders'),
)
