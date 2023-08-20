from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from market_dashbord.views import *

app_name = 'market_dashbord'

urlpatterns = [
    path('show_all_markets', show_all_markets, name='show_all_markets'),
    path('show_my_market', show_my_market, name='show_my_market'),
    path('market_detail/<int:pk>/', show_market, name='market_detail'),
    path('new-market', create_new_market, name='create_new_market'),
    path('show_contacts', show_contacts, name='show_contacts'),
    path('show_6_day_food', show_6_day_food, name='show_6_day_food'),
    path('show_30_day_food', show_30_day_food, name='show_30_day_food'),
    path('create_food_record', create_food_record, name='create_food_record'),
    path('write_off_product/<int:pk>/', write_off_product, name='write_off_product'),
    path('show_write_off', show_write_off, name='show_write_off'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)