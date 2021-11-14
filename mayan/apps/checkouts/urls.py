from __future__ import unicode_literals

from django.conf.urls import url

from .api_views import APICheckedoutDocumentListView, APICheckedoutDocumentView
from .views import (
    CheckoutDocumentView, CheckoutDetailView, CheckoutListView,
    DocumentCheckinView
)

urlpatterns = [
    url(r'^list/$', CheckoutListView.as_view(), name='checkout_list'),
    url(
        r'^(?P<pk>\d+)/check/out/$', CheckoutDocumentView.as_view(),
        name='checkout_document'
    ),
    url(
        r'^(?P<pk>\d+)/check/in/$', DocumentCheckinView.as_view(),
        name='checkin_document'
    ),
    url(
        r'^(?P<pk>\d+)/check/info/$', CheckoutDetailView.as_view(),
        name='checkout_info'
    ),
]

api_urls = [
    url(
        r'^checkouts/$', APICheckedoutDocumentListView.as_view(),
        name='checkout-document-list'
    ),
    url(
        r'^checkouts/(?P<pk>[0-9]+)/checkout_info/$', APICheckedoutDocumentView.as_view(),
        name='checkedout-document-view'
    ),
]
