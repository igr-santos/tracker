from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
]
