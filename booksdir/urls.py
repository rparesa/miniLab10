from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from booksdir import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'add/$',views.book_add),
    url(r'^books/(?P<pk>[0-9]+)/$', views.book_details),
]
urlpatterns = format_suffix_patterns(urlpatterns)
