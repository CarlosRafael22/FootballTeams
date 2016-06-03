"""MyTeams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from website import views
from rest_framework.urlpatterns import format_suffix_patterns


team_urls = patterns('',
	url(r'^/(?P<pk>[0-9]+)$', views.TeamDetail.as_view(), name='team_detail'),
	url(r'^$', views.TeamList.as_view(), name='team_list')
)

player_urls = patterns('',
	url(r'^/(?P<pk>[0-9]+)$', views.PlayerDetail.as_view(), name='player_detail'),
	url(r'^$', views.PlayerList.as_view(), name='player_list')
)

user_urls = patterns('',
    url(r'^/(?P<pk>[0-9]+)$',views.UserDetail.as_view(), name='user_detail'),
    url(r'^$', views.UserList.as_view(), name='user_list')
)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teams', include(team_urls)),
    url(r'^players', include(player_urls)),
    url(r'^users', include(user_urls)),
    # url(r'^home',views.UserFormView.as_view()),
    url(r'^signup',views.signup),
    url(r'^login',views.logIn),
    url(r'^logout',views.logOut),
    url(r'^createTeam',views.createTeam),
    url(r'^createPlayer',views.createPlayer),
    url(r'^$',views.home_view),
    
    url(r'^getTeam',views.getTeam),
    url(r'^getUser',views.getUser),
    url(r'^getPlayers',views.getPlayers),
    url(r'^updatePlayer',views.updatePlayer),
]


urlpatterns = format_suffix_patterns(urlpatterns)