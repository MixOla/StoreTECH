from rest_framework import serializers

from firm.models import Firm


class FirmSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Firm
        fields = '__all__'


        