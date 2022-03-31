from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # Example: /blog/
    path('', views.PostLV.as_view(), name='index'),

    # Example: /blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),

    # Example: /blog/post/django-example/ 한글도 인식 가능
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # Example: /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Example: /blog/archive/2022/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Example: /blog/archive/2022/jan/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # Example: /blog/archive/2022/jan/09/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # Example: /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    path('add/', views.PostCreateView.as_view(), name='add'),

    path('change/', views.PostChangeLV.as_view(), name='change'),

    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),

    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    ]
