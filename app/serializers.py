from rest_framework import serializers

from app.models import Country, Category, Title


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id": instance.pk,
            "name": instance.name,
            "type": instance.type,
            "date_added": instance.date_added,
            "description": instance.description,
            "duration": instance.duration,
            "release_year": instance.release_year,
            "countries": [
                {'id': country.id, 'name': country.name}
                for country in instance.countries.all()
            ],
            "categories": [
                {'id': category.id, 'name': category.name}
                for category in instance.categories.all()
            ],
        }