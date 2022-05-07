from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = 'essential'

urlpatterns = [
                  path('', views.dashboard, name='dashboard'),
                  path('expense_list/', views.expense_list, name='expense_list'),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path('signup/', views.register, name='signup'),
                  path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
                  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
                       name='password_change_done'),
                  path('password_reset/',
                       auth_views.PasswordResetView.as_view(),
                       name='password_reset'),
                  path('password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),
                  path('reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(),
                       name='password_reset_complete'),
                  path('expense/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
                  path('expense/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
                  path('income_list/', views.income_list, name='income_list'),
                  path('income/<int:pk>/edit/', views.income_edit, name='income_edit'),
                  path('income/<int:pk>/delete/', views.income_delete, name='income_delete'),
                  path('expense/create/', views.expense_new, name='expense_new'),
                  path('income/create/', views.income_new, name='income_new'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
