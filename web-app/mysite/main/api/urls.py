from django.urls import re_path

from . import views
app_name = 'main'
urlpatterns = [
    re_path(r'^products/$', views.SubjectListView.as_view(), name='order_list'),
    re_path(r'^products/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='order_detail'),
]