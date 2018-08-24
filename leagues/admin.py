from django.contrib import admin

from .models import League, Division, Fixture, Player, Team, Season, Match

class DivisionInline(admin.StackedInline):
    model = Division
    extra = 1

class LeagueAdmin(admin.ModelAdmin):
    fields = ['league_name']

class TeamInline(admin.TabularInline):
    model = Team
    extra = 1

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['get_league_name', 'division_number']
    list_filter = ['season__league__league_name']
    inlines = [TeamInline]

    def get_league_name(self, obj):
        return obj.season.league.league_name

    get_league_name.short_description = 'League'
    get_league_name.admin_order_field = 'season__league__league_name'

class MatchInline(admin.TabularInline):
    model = Match
    extra = 0

class FixtureAdmin(admin.ModelAdmin):
    inlines = [MatchInline]

# Register your models here.
admin.site.register(League, LeagueAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Season)
admin.site.register(Fixture, FixtureAdmin)
