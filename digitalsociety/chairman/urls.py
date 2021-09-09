"""digitalsociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('logout/', views.logout, name='logout'),
    path('chairman-profile/', views.chairman_profile, name='chairman-profile'),
    path('reset-profile-password/', views.reset_profile_password, name='reset-profile-password'),
    path('reset-profile/', views.reset_profile, name='reset-profile'),
    path('add-member/', views.add_member, name='add-member'),
    path('view-member/', views.view_member, name='view-member'),
    path('view-member1/', views.view_member1, name='view-member1'),
    path('view-member-profile/<int:pk>', views.view_member_profile, name='view-member-profile'),
    path('view-member-profile1/<int:pk>', views.view_member_profile1, name='view-member-profile1'),
    path('notice/', views.notice, name='notice'),
    path('notice-view/', views.notice_view, name='notice-view'),
    path('delete-notice/<int:pk>', views.delete_notice, name='delete-notice'),
    path('view-watchman/', views.view_watchman, name='view-watchman'),
    path('add-watchman/', views.add_watchman, name='add-watchman'),
    path('view-watchman-profile/<int:pk>', views.view_watchman_profile, name='view-watchman-profile'),
    path('member-profile/', views.member_profile, name='member-profile'),
    path('reset-profile1-password/', views.reset_profile1_password, name='reset-profile1-password'),
    path('reset-profile1/', views.reset_profile1, name='reset-profile1'),
    path('watchman-profile/', views.watchman_profile, name='watchman-profile'),
    path('reset-profile2-password/', views.reset_profile2_password, name='reset-profile2-password'),
    path('reset-profile2/', views.reset_profile2, name='reset-profile2'),
    path('notice1-view/', views.notice1_view, name='notice1-view'),
  
    path('notice2-view/', views.notice2_view, name='notice2-view'),
    path('event/', views.event, name='event'),
    path('event-view/', views.event_view, name='event-view'),
    path('delete-event/<int:pk>', views.delete_event, name='delete-event'),
    path('event1-view/', views.event1_view, name='event1-view'),
  
    path('event2-view/', views.event2_view, name='event2-view'),
    path('member-complaint/', views.member_complaint, name='member-complaint'),
    path('mycomplaint1/', views.mycomplaint1, name='mycomplaint1'),
    path('delete-mycomplaint1/<int:pk>', views.delete_mycomplaint1, name='delete-mycomplaint1'),
    path('mycomplaint2/', views.mycomplaint2, name='mycomplaint2'),
    path('delete-mycomplaint2/<int:pk>', views.delete_mycomplaint2, name='delete-mycomplaint2'),
    path('watchman-complaint/', views.watchman_complaint, name='watchman-complaint'),
    path('member-complaint-view/', views.member_complaint_view, name='member-complaint-view'),
    path('watchman-complaint-view/', views.watchman_complaint_view, name='watchman-complaint-view'),
    path('add-visitors/', views.add_visitors, name='add-visitors'),
    path('view-visitors/', views.view_visitors, name='view-visitors'),
    path('view-visitors2/', views.view_visitors2, name='view-visitors2'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('callback/', views.callback, name='callback'),
    path('maintenance-details/', views.maintenance_details, name='maintenance-details'),
    # path('',views.landing_page,name='landing-page'),
    path('web-visitor/', views.web_visitor, name='web-visitor'),
    path('reset-forgot-password/', views.reset_forgot_password, name='reset-forgot-password'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('contact-list/', views.contact_list, name='contact-list'),
    path('contact1-list/', views.contact1_list, name='contact1-list'),
    path('contact2-list/', views.contact2_list, name='contact2-list'),
    path('view-chairman1/', views.view_chairman1, name='view-chairman1'),
    path('view-chairman2/', views.view_chairman2, name='view-chairman2'),

]
