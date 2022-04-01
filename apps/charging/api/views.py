from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import ChargingSerializer
from csms.utils import truncate
from ..components import (
    EnergyCalculatorComponent,
    TimeCalculatorComponent,
    TransactionCalculatorComponent,
    ChargingPriceCalculator,
)


class ChargeHandlingView(APIView):
    @swagger_auto_schema(method="POST", request_body=ChargingSerializer)
    @action(methods=["POST"], detail=False)
    def post(self, request, format=None):
        serializer = ChargingSerializer(data=request.data)
        if serializer.is_valid():
            response = dict()
            energy_calculator = EnergyCalculatorComponent(
                energy=serializer.validated_data["rate"]["energy"],
                meter_start=serializer.validated_data["cdr"]["meterStart"],
                meter_stop=serializer.validated_data["cdr"]["meterStop"],
            )
            time_calculator = TimeCalculatorComponent(
                time=serializer.validated_data["rate"]["time"],
                time_start=serializer.validated_data["cdr"]["timestampStart"],
                time_stop=serializer.validated_data["cdr"]["timestampStop"],
            )
            transaction_calculator = TransactionCalculatorComponent(
                transaction=serializer.validated_data["rate"]["transaction"],
            )
            response["components"] = ChargingPriceCalculator(
                {
                    "energy": energy_calculator,
                    "time": time_calculator,
                    "transaction": transaction_calculator,
                }
            ).calculate_price()

            for component in response["components"].keys():
                response["components"][component] = float(
                    truncate(response["components"][component], 2)
                )
            response["overall"] = float(
                truncate(sum(response["components"].values()), 2)
            )
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
