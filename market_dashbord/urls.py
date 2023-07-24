from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from market_dashbord.views import create_new_market, show_market, show_my_market, show_all_markets

app_name = 'market_dashbord'

urlpatterns = [
    path('show_all_markets', show_all_markets, name='show_all_markets'),
    path('show_my_market', show_my_market, name='show_my_market'),
    path('market_detail/<int:pk>/', show_market, name='market_detail'),
    path('new-market', create_new_market, name='create_new_market'),
    # path('employee/register/', views.employee_registration, name='employee-registration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)