from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('edit/', views.edit, name='edit'),

    # path('employee/register/', views.employee_registration, name='employee-registration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
