from django.conf.urls import include, url

from django.contrib import admin

from lots_client.views import home, status, apply, apply_confirm, faq, about

from lots_admin.views import lots_admin, lots_admin_map, csv_dump, lots_login, lots_logout

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^status/$', status, name='status'),
    url(r'^apply/$', apply, name='apply'),
    url(r'^apply-confirm/(?P<tracking_id>\S+)/$', apply_confirm, name='apply_confirm'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^about/$', about, name='about'),
    url(r'^lots-admin/$', lots_admin, name='lots_admin'),
    url(r'^lots-admin-map/$', lots_admin_map, name='lots_admin_map'),
    url(r'^csv-dump/$', csv_dump, name='csv_dump'),
    url(r'^lots-login/$', lots_login, name='lots_login'),
    url(r'^logout/$', lots_logout, name='logout'),

    url(r'^django-admin/', admin.site.urls),
]
