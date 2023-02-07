from django.contrib import admin
from .models import Stock
from .models import Broker
from .models import Risk
from .models import Probability
from .models import Investment
from .models import Briefcase

# Register your models here.

admin.site.register(Stock)
admin.site.register(Broker)
admin.site.register(Risk)
admin.site.register(Probability)
admin.site.register(Investment)
admin.site.register(Briefcase)