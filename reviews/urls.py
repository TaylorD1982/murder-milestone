from django.conf.urls import url
from .views import get_reviews, review_detail, create_or_edit_review

urlpatterns = [
    url(r'^$', get_reviews, name='get_reviews'),
    url(r'^(?P<pk>\d+)/$', review_detail, name='review_detail'),
    url(r'^new/$', create_or_edit_review, name='new_review'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_review, name='edit_review')
]