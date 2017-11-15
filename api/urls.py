from django.conf.urls import url
from .views import register, get_top, pop_queue, pop_retry, requeue, get_skipped

urlpatterns = [
    url(r'^register/', register, name="register"),
    url(r'^top/', get_top, name="get_top"),
    url(r'^pop-queue/', pop_queue, name="pop_queue"),
    url(r'^pop-retry/', pop_retry, name="pop_retry"),
    url(r'^requeue/', requeue, name="requeue"),
    url(r'^get-skipped/', get_skipped, name="get_skipped"),
]
