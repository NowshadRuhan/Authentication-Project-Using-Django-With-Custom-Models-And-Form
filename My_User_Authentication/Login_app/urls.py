from django.conf.urls import url
from django.urls import path
from Login_app import views

# #settings added
from django.conf import settings
# # #static and static_url added
from django.conf.urls.static import static


app_name = 'Login_app'

urlpatterns = [
    path('', views.index, name='Home'),
    path('signup/', views.register, name='register' ),
    path('signin/', views.login_page, name='login'),
    path('user_login/', views.user_login, name='userLogin'),
    path('logout/', views.user_logout, name='logout'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
