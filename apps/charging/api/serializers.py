from rest_framework import serializers
import json
from csms.utils import datetime_iso


class RateSerializer(serializers.Serializer):
    energy = serializers.FloatField()
    time = serializers.IntegerField()
    transaction = serializers.IntegerField()


class CDRSerializer(serializers.Serializer):
    meterStart = serializers.IntegerField()
    timestampStart = serializers.DateTimeField()
    meterStop = serializers.IntegerField()
    timestampStop = serializers.DateTimeField()

    def validate(self, attrs):
        if attrs['meterStart'] > attrs['meterStop']:
            raise serializers.ValidationError("Meter start must be less than meter stop")
        return super().validate(attrs)


class ChargingSerializer(serializers.Serializer):
    rate = RateSerializer()
    cdr = CDRSerializer()
