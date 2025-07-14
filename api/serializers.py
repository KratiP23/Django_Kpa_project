from rest_framework import serializers
from .models import WheelSpecification

class WheelSpecificationSerializer(serializers.ModelSerializer):
    nested_fields = serializers.SerializerMethodField()

    class Meta:
        model = WheelSpecification
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'nested_fields']

    def get_nested_fields(self, obj):
        return {
            "treadDiameterNew": obj.treadDiameterNew,
            "lastShopIssueSize": obj.lastShopIssueSize,
            "condemningDia": obj.condemningDia,
            "wheelGauge": obj.wheelGauge,
            "variationSameAxle": obj.variationSameAxle,
            "variationSameBogie": obj.variationSameBogie,
            "variationSameCoach": obj.variationSameCoach,
            "wheelProfile": obj.wheelProfile,
            "intermediateWWP": obj.intermediateWWP,
            "bearingSeatDiameter": obj.bearingSeatDiameter,
            "rollerBearingOuterDia": obj.rollerBearingOuterDia,
            "rollerBearingBoreDia": obj.rollerBearingBoreDia,
            "rollerBearingWidth": obj.rollerBearingWidth,
            "axleBoxHousingBoreDia": obj.axleBoxHousingBoreDia,
            "wheelDiscWidth": obj.wheelDiscWidth
        }

    def create(self, validated_data):
        fields_data = self.context['request'].data.get('fields', {})
        validated_data.update(fields_data)
        return WheelSpecification.objects.create(**validated_data)
