from django.contrib import admin

# Register your models here.
from sport.models import *

admin.site.register(BasketballTeam)
admin.site.register(BasketballEvent)
admin.site.register(BasketballGame)
admin.site.register(BasketballNonPlayer)
admin.site.register(BasketballPlayer)
admin.site.register(BasketballLeague)

admin.site.register(FootballPlayer)
admin.site.register(FootballEvent)
admin.site.register(FootballGame)
admin.site.register(FootballNonPlayer)
admin.site.register(FootballTeam)
admin.site.register(FootballLeague)
admin.site.register(FootballImage)
admin.site.register(FootballVideo)

admin.site.register(FootballTeamInFootballGame)
admin.site.register(FootballPlayerInFootballGame)

admin.site.register(BasketballTeamInBasketballGame)
admin.site.register(BasketballPlayerInBasketballGame)

admin.site.register(BasketballImage)
admin.site.register(BasketballVideo)


class NewsAdmain(admin.ModelAdmin):
    list_display = ('publish_date', 'title', 'type')
    list_filter = ('type',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmain)


class ResourceAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'writer')

    search_fields = ('title',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Resource)

admin.site.register(Tag)

# ---------------------------------------------
# class FoodAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'create_date', 'picture', 'image_tag')
#     list_filter = ('create_date',)
#     search_fields = ('name', 'description', 'create_date')
#
#
# @admin.register(Reserve)
# class ReserveAdmin(admin.ModelAdmin):
#     list_display = ['user', 'food', 'reserve_date', 'type']
#     list_filter = ['user', 'food', 'type', 'reserve_date']
#
# admin.site.register(Food, FoodAdmin)
