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
    (r'users', UserViewSetV1, 'users'),
    (r'activities', ActivityViewSetV1, 'activities'),
    (r'cities', CityViewSetV1, 'cities'),
    (r'kinds', KindViewSetV1, 'kinds'),
    (r'social_accounts', SocialAccountViewSetV1, 'social_accounts')
]

for router in LIST_V1:
    router_V1.register(router[0], router[1], base_name=router[2])


urlpatterns = [
    url(r'v1/', include(router_V1.urls, namespace='v1')),
]
