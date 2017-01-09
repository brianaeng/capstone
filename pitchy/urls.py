from django.conf.urls import url
from . import views
# from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#urlpatterns = [
    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    # url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    # # url(r'^$', views.HomepageView.as_view(), name='homepage'),
    # url(r'^profile/edit/$', views.UpdateProfileView.as_view(), name='update_profile'),
    # url(r'^hub/$', views.HubView.as_view(), name='hub'),
    # url(r'^user/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile'),
    # url(r'^messages/(?P<pk>\d+)/$', views.ConversationView.as_view(), name='messages'),
#]
