from xml.etree.ElementInclude import include
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.http import HttpResponse
from django.conf.urls.static import static
# from members.urls import urlpatterns

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('display',views.display,name="display"),
    path('login',views.login,name="login"),
    path('landing',views.landing,name="landing"),
    path('subjects3',views.subjects3,name="subjects3"),
    path('subjects4',views.subjects4,name="subjects4"),
    path('subjects5',views.subjects5,name="subjects5"),
    path('subjects6',views.subjects6,name="subjects6"),
    path('subjects3c',views.subjects3c,name="subjects3c"),
    path('subjects6c',views.subjects6c,name="subjects6c"),
    path('final',views.final,name="final"),
    path('demo',views.demo,name="demo"),

    path('display',views.display,name="display"),
    # path('C:/Users/vinod/Dev/static/css/images/',views.images,name='images')
    # path('display',views.display,name="dispay"),
    path('add_faculty',views.add_faculty,name="add-faculty"),
    path('add_users',views.add_users,name="add-users"),
    path('add_usersc',views.add_usersc,name="add-usersc"),
    path('add_committee',views.add_committee,name="add-committee"),
    path('landingc',views.landingc,name="landingc"),
    path('loginc',views.loginc,name="loginc"),
    path('sub_image',views.sub_image,name="sub-image"),
    path('show_image',views.show_image,name="show-image"),
    # path('register_user',views.register_user,name="register-user"),
    path('register_user',views.register_user,name="register_user"),
    path('login_user',views.login_user,name='login'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
