from django.contrib import admin

from .models import Team, TeamMember, Standup, Question, StandupQuestion, Session, SessionMember, SessionMemberAnswer


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'server', 'discord_channel_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'server', 'created_at')
    search_fields = ('name', 'discord_channel_id', 'server__name')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('server', 'name', 'discord_channel_id', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'discord_user_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'team', 'team__server', 'created_at')
    search_fields = ('name', 'discord_user_id', 'team__name', 'team__server__name')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('team', 'name', 'discord_user_id', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(Standup)
class StandupAdmin(admin.ModelAdmin):
    list_display = ('team', 'start_time', 'finish_time', 'schedule', 'is_active', 'created_at')
    list_filter = ('is_active', 'team', 'team__server', 'created_at')
    search_fields = ('team__name', 'team__server__name')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('team', 'start_time', 'finish_time', 'schedule', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    ordering = ('order',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(StandupQuestion)
class StandupQuestionAdmin(admin.ModelAdmin):
    list_display = ('standup', 'question', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'standup__team', 'created_at')
    search_fields = ('standup__team__name', 'question__title')
    ordering = ('standup', 'order')
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('standup', 'question', 'order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('standup', 'started_at', 'finished_at', 'discord_message_id', 'created_at')
    list_filter = ('standup__team', 'started_at', 'finished_at')
    search_fields = ('standup__team__name', 'discord_message_id')
    ordering = ('-started_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('standup', 'started_at', 'finished_at', 'discord_message_id')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(SessionMember)
class SessionMemberAdmin(admin.ModelAdmin):
    list_display = ('session', 'team_member', 'finished_at', 'discord_message_id', 'created_at')
    list_filter = ('session__standup__team', 'finished_at', 'created_at')
    search_fields = ('session__standup__team__name', 'team_member__name')
    ordering = ('session', 'team_member')
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('session', 'team_member', 'finished_at', 'discord_message_id')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )


@admin.register(SessionMemberAnswer)
class SessionMemberAnswerAdmin(admin.ModelAdmin):
    list_display = ('session_member', 'standup_question', 'value', 'created_at')
    list_filter = ('session_member__session__standup__team', 'created_at')
    search_fields = ('session_member__team_member__name', 'standup_question__question__title', 'value')
    ordering = ('session_member', 'standup_question')
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('session_member', 'standup_question', 'value')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )
