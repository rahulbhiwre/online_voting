from django.contrib import admin
from django.urls import path,include
from members import views
from members.views import SignUpView, home, vote, validateotp,voted,result
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('home/', home.as_view(), name='home'),
    path('result/', result, name='result'),
    path('validateotp/', validateotp, name="validateotp"),
    path('vote/<user_id>/',vote, name='vote'),
    path('voted/',home.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='thanks'),name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"),name="password_reset_complete"),

]
