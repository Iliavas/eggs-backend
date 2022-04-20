from rest_framework.serializers import ModelSerializer
from .models import Top


class TopSerializer(ModelSerializer):
    class Meta:
        model = Top
        fields = ("value", "nickname")

    def create(self, validated_data):
        print(validated_data)
        value = validated_data['value']
        nick = validated_data['nickname']
        sorted_top = Top.objects.order_by('value')
        if len(Top.objects.all()) > 50:
            if sorted_top.first().value > value: return {}
            sorted_top.first().delete()
        return Top.objects.create(nickname=nick, value=value)
