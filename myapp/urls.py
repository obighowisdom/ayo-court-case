from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
# from tradeApp.forms import UserLoginForm
from .views import CustomLoginView, SignUpView


app_name = 'myappurl'

urlpatterns = [
    path('', views.index, name = 'index'),
 
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('opinion/', views.opinion, name='opinion'),
    path('filing/', views.filing, name='filing'),
    path('case/', views.case, name='case'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('oral/', views.oral, name='oral'),
    path('case/<str:access_code>/', views.access_case, name='access_case'),

    
]