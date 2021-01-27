from app.models import Country, Movie, Category

Movie.objects.all().delete()
Country.objects.all().delete()
Category.objects.all().delete()


