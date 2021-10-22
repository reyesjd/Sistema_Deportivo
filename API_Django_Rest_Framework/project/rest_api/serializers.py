from rest_framework import serializers
from rest_api.models import Equipo, Partido


class SerializadorEquipo(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

    def update(self, instance, validated_data):
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance


class SerializadorPartido(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

    def update(self, instance, validated_data):
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance
