from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)
# При регистрации эндпоинтов с таким URL-префиксом
# router.register(r'profile/(?P<username>[\w.@+-]+)/', AnyViewSet)
# ...вьюсет AnyViewSet будет получать на обработку все запросы с адресов
# /profile/toh@/
# /profile/nik.nik/
# /profile/leo/
# ...и подобных, ограниченных маской регулярного выражения.

urlpatterns = [
    path('', include(router.urls)),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]
