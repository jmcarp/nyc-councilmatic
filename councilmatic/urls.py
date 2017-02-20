from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from haystack.query import EmptySearchQuerySet
from councilmatic_core.views import CouncilmaticSearchForm
from nyc.views import *  # noqa
from nyc.feeds import *  # noqa

patterns = ([
    url(r'^committees/$', NYCCommitteesView.as_view(), name='committees'),
    url(r'^committee/(?P<slug>[^/]+)/$', NYCCommitteeDetailView.as_view(), name='committee_detail'),
    url(r'^person/(?P<slug>[^/]+)/$', NYCPersonDetailView.as_view(), name='person'),
    url(r'^search/rss/',
        NYCCouncilmaticFacetedSearchFeed(), name='councilmatic_search_feed'),
    url(r'^search/', NYCCouncilmaticFacetedSearchView(searchqueryset=EmptySearchQuerySet,
                                       form_class=CouncilmaticSearchForm), name='search'),
    url(r'^$', NYCIndexView.as_view(), name='index'),
    url(r'^about/$', NYCAboutView.as_view(), name='about'),
    url(r'^legislation/(?P<slug>[^/]+)/$', NYCBillDetailView.as_view(), name='bill_detail'),
    url(r'^legislation/(?P<slug>[^/]+)/widget/$', NYCBillWidgetView.as_view(), name='bill_widget'),
    url(r'^legislation/(?P<slug>[^/]+)/rss/$', NYCBillDetailActionFeed(), name='bill_detail_action_feed'),
], settings.APP_NAME)

urlpatterns = [
    url(r'', include(patterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('councilmatic_core.urls')),
]
