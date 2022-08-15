from django.contrib import admin
from .models import *

class BookInline(admin.TabularInline):
    model = TozihPlan

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
        

admin.site.register(Tag)
admin.site.register(SiteSetting)
admin.site.register(Head)
admin.site.register(ZirHead)
admin.site.register(Khadamat)
admin.site.register(PricePlan,AuthorAdmin)
# admin.site.register(TozihPlan)
admin.site.register(Advice)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(HistoryRight)
admin.site.register(HistoryLeft)
admin.site.register(Call)

