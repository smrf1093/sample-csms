from django.urls import path
from .views import ChargeHandlingView

app_name="charging"

urlpatterns = [
    path('charging/', ChargeHandlingView.as_view(), name='charge-handing'),
]


