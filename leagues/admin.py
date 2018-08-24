from django.contrib import admin

from .models import League, Division, Fixture, Player, Team

class DivisionInline(admin.StackedInline):
    model = Division
    extra = 1

class LeagueAdmin(admin.ModelAdmin):
    fields = ['league_name']
    inlines = [DivisionInline]

class TeamInline(admin.TabularInline):
    model = Team
    extra = 1

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['get_league_name', 'division_number']
    list_filter = ['league__league_name']
    inlines = [TeamInline]

    def get_league_name(self, obj):
        return obj.league.league_name

    get_league_name.short_description = 'League'
    get_league_name.admin_order_field = 'league__league_name'

# Register your models here.
admin.site.register(League, LeagueAdmin)
admin.site.register(Division, DivisionAdmin)
# admin.site.register(Player)
# admin.site.register(Team)
# admin.site.register(Fixture)
