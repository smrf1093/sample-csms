from urllib import request
from django.test import TestCase, RequestFactory
from charging.api.views import ChargeHandlingView

# Create your tests here.
class TestCharging(TestCase):
    def test_charge_handling(self):

        view = ChargeHandlingView()
        request = RequestFactory()
        request.data = {
            "rate": {"energy": 0.3, "time": 2, "transaction": 1},
            "cdr": {
                "meterStart": 1204307,
                "timestampStart": "2021-04-05T10:04:00Z",
                "meterStop": 1215230,
                "timestampStop": "2021-04-05T11:27:00Z",
            },
        }

        response = view.post(request=request)
        print(response.data)
        self.assertEqual(response.data['overall'], 7.02)
        self.assertEqual(response.data['components']['energy'], 3.27)
        self.assertEqual(response.data['components']['time'], 2.76)
        self.assertEqual(response.data['components']['transaction'], 1.0)
        self.assertEqual(response.status_code, 200)
