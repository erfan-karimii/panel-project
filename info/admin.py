from django.contrib import admin

# Register your models here.
from .models import Activity,Circle,DetailProfile,Line,Profile


admin.site.register(Activity)
admin.site.register(Circle)
admin.site.register(DetailProfile)
admin.site.register(Line)
admin.site.register(Profile)
