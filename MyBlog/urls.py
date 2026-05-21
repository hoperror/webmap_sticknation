from django.urls import path
from . import views

app_name = 'MyBlog' # Très important pour les balises {% url %}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('explorer/', views.explorer, name='explorer'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('<int:id>/<slug:slug>/', views.post_detail, name='post_detail'),
    
    # Les APIs pour la carte et les likes
    path('api/sticks/', views.stick_api, name='stick_api'),
    path('api/layer/<int:id>/', views.get_geojson, name='api_get_geojson'),
    path('api/like/<int:id>/', views.like_stick, name='api_like_stick'),
]