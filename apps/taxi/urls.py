from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestViewSet, ActiveRequestSearchView, GetRequestViewSet, BalansYechishViewSet, \
    BalansToldirishViewSet, AdvertisementViewSet

router = DefaultRouter()
router.register(r'requests', RequestViewSet)
router.register(r'getrequests', GetRequestViewSet)
router.register(r'add_balance', BalansToldirishViewSet, basename='add_balance')
router.register(r'remove_balance', BalansYechishViewSet, basename='remove_balance')
router.register(r'reklama', AdvertisementViewSet, basename='reklama')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', ActiveRequestSearchView.as_view(), name='request-search'),
]