from django.urls import include, path
from rest_framework_nested.routers import SimpleRouter

from .views import download_excel_view, ClientsViewSet, BillsViewSet


router_v1 = SimpleRouter()
router_v1.register("clients", ClientsViewSet, basename="clients")
router_v1.register("bills", BillsViewSet, basename="bills")


urlpatterns = [
    path(r"", include(router_v1.urls)),
    path('download/', download_excel_view)
]
