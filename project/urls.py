from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from project.apps.twyla import views
from django.contrib.auth.decorators import login_required

urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/home')),
    url(r'^home/$', login_required(views.Home.as_view()), name='home'),
    url(r'^books/list$', login_required(views.BookList.as_view()), name='book_list'),
    url(r'^books/$', login_required(views.BookCreate.as_view()), name='book_create'),
    url(r'^books/(?P<book_id>\w+)/review$', login_required(views.BookReview.as_view()), name='book_review'),
    #url(r'^rates/$', views.AddRate.as_view(), name='add_rate'),

    # auth
    url(r'^login/?$', views.Login.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', RedirectView.as_view(url='/api')),
    url(
        r'^api/',
        include(
            ('project.apps.twyla.api.urls', 'twyla'),
            namespace='twyla_api'),
    ),
)
