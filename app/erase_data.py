from app.models import Country, Title, Category

Title.objects.all().delete()
Country.objects.all().delete()
Category.objects.all().delete()


