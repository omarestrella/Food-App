from django.conf.urls.defaults import patterns, include
import views

from views import HomepageView

urlpatterns = ('',
    (r'^', views.HomepageView.as_view(), name='url_homepage'),
    (r'^', views.ItemListView.as_view(), name='url_items')
)
