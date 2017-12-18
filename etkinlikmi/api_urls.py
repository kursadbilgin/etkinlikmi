# Django
from django.conf.urls import url, include

# Third-Party
from rest_framework import routers

# Local Django
from user.api_views import UserViewSetV1
from core.api_views import CityViewSetV1, KindViewSetV1, SocialAccountViewSetV1
from activity.api_views import ActivityViewSetV1


router_V1 = routers.DefaultRouter()

LIST_V1 = [
    (r'user', UserViewSetV1, 'user'),
    (r'activity', ActivityViewSetV1, 'activity'),
    (r'city', CityViewSetV1, 'city'),
    (r'kind', KindViewSetV1, 'kind'),
    (r'social_account', SocialAccountViewSetV1, 'social_account')
]

for router in LIST_V1:
    router_V1.register(router[0], router[1], base_name=router[2])


urlpatterns = [
    url(r'v1/', include(router_V1.urls, namespace='v1')),
]
