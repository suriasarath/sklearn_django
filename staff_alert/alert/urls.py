from django.urls import path,include
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns =[

    path('input',views.input,name='input'),
    path('',views.Index.as_view(),name='home'),
    path('output',views.output,name='output'),
    #path('analy/<int:pk1>',views.analy,name='output'),
    path('analy',views.analy_list,name='output'),
    path('algorithms/',views.algorithms,name='algorithms'),
    path('algorithms/<int:pk>', views.dash, name='algorithms'),
    path('algorithms/<int:pk>/predict',views.csv_json,name = 'predict'),
    path('algorithms/<int:pk>/chart',views.Chart.as_view(),name = 'chart'),

    path('signup',views.Signup.as_view(),name='signup'),
    path('lists', views.lists.as_view(),name='lists'),
    path('lists/<int:pk1>',views.analy,name='output'),



    path('accounts/login/',LoginView.as_view(template_name='account.html',redirect_field_name='lists'),name='login'),
    path('accounts/logout',views.logout,name='logout'),
    path('accounts/password_change/ ',PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('accounts/password_reset/',PasswordResetView.as_view(template_name='account.html'),name='password_reset'),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name = 'password_reset_confirm'),
    #path('accounts/reset/done/',PasswordResetDoneView.as_view(),name = 'password_reset_complete')
]


