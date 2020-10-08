from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .forms import MyAuthenticationForm

urlpatterns = [
    path('student/register', views.student_register,name='student-register'),
    path('contact/<int:pk>', views.contact_user,name='user-profile'),
    path('profile/', views.profile , name='profile'),
    path('editpro/', views.edit_profile , name='edit-profile'),
    path('login/', LoginView.as_view(template_name='login.html',authentication_form = MyAuthenticationForm),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
]