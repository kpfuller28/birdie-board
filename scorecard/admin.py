from django.contrib import admin
from .models import User, Round, Hole


class HoleInline(admin.TabularInline):
    model = Hole
    extra = 9


class RoundAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Par & Score Totals", {
            "fields": ['score', 'nine_par', 'full_par'],
            "classes": ["collapse"]
        }),
        ("Round Info", {
            "fields": ['holes', 'date', 'user']
        }),
    ]
    readonly_fields = ['score', 'nine_par', 'full_par', 'holes']
    inlines = [HoleInline]
    def save_related(self, request, form, formsets, change):
        # Save holes first
        super().save_related(request, form, formsets, change)
        # Then recalculate the Round data with up-to-date holes
        form.instance.save()

admin.site.register(User)
admin.site.register(Round, RoundAdmin)
admin.site.register(Hole)
