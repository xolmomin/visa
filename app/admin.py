from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import PUser, Winner, Member


@admin.register(PUser)
class PUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'confirm_number', 'birth', 'won')
    fields = ('confirm_number', 'name', 'birth', 'won')
    search_fields = ('confirm_number',)


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'case_number', 'confirm_number', 'birth_date')
    fields = ['name', 'lastname', 'address', 'case_number', 'confirm_number', 'birth_date', 'status', 'member']
    search_fields = ('confirm_number',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "p_user":
            winner_id = request.path.split('/')[4]
            if winner_id.isdigit():
                winner = Winner.objects.get(pk=winner_id)
                kwargs["queryset"] = Winner.objects.filter(id__in=winner.member.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# admin.site.register(Winner, WinnerAdmin)
admin.site.register(Member)
admin.site.unregister(Group)
admin.site.unregister(User)
