import django_tables2 as tables
from .models import City


class CityTable(tables.Table):

    class Meta:
        model = City
        fields        = ('name',)
        template_name = 'django_tables2/bootstrap4.html'
