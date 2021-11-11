from rest_framework.routers import DefaultRouter
from leads.api import LeadViewset

router = DefaultRouter()
router.register(r'api/leads', LeadViewset)

urlpatterns = router.urls
