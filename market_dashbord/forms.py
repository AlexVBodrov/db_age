from django.forms import ModelForm
from market_dashbord.models import Market

class MarketForm(ModelForm):
    class Meta:
        model = Market

        fields = ['number_market']