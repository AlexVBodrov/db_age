from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users import views
from django.views.defaults import server_error, page_not_found, permission_denied


app_name = 'product'

urlpatterns = [

    # path('employee/register/', views.employee_registration, name='employee-registration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
