from django.urls import path
from .views import CreateViewPage
from . import views
app_name = 'page'
urlpatterns = [
    path('', views.LandingPage, name='landing_page'),
    path('blog', views.BlogPage, name='blogpage'),
    path('post/<slug:slug>/', views.DetailPage, name='detailpage'),
    path('user/', views.UserView, name='userpage'),
    path('addnewpost/', CreateViewPage.as_view(), name='newpost')

]