from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup', views.signupsystem, name='signupsystem'),
    path('login', views.loginsystem, name='loginsystem'),
    path('logout', views.logout_view, name='logout'),
    path('profileo', views.profileo, name='po'),
    path('stories', views.stories, name='stories'),
    path('stories/<int:story_id>/', views.story_detail, name='story_detail'),
    path('communities', views.communities, name='communities'),
    path('communities/<int:community_id>/', views.community_detail, name='community_detail'),
    path('create_story', views.create_story, name='create_story'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
