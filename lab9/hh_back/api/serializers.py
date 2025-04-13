from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    salary = serializers.FloatField()

    def create(self, validated_data):
        return Vacancy.objects.create(**validated_data)

