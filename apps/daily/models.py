from django.db import models

from apps.core.models import BaseModel
from apps.bot.models import Server


class Team(BaseModel):
    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        help_text="Discord server this team belongs to"
    )
    name = models.CharField(
        max_length=255,
        help_text="Team name"
    )
    discord_channel_id = models.CharField(
        max_length=20,
        help_text="Discord channel ID where bot will send messages"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Should daily bot be active for this team?"
    )

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        unique_together = ['server', 'name']

    def __str__(self):
        return f"{self.name} ({self.server.name})"


class TeamMember(BaseModel):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        help_text="Team this member belongs to"
    )
    discord_user_id = models.CharField(
        max_length=20,
        help_text="Discord user ID"
    )
    name = models.CharField(
        max_length=255,
        help_text="Member name"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Is this member active in the team?"
    )

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
        unique_together = ['team', 'discord_user_id']

    def __str__(self):
        return f"{self.name} ({self.team.name})"


class Question(BaseModel):
    title = models.CharField(
        max_length=255,
        help_text="Question title"
    )
    order = models.PositiveIntegerField(
        help_text="Order in which the question should be asked"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Is this question active?"
    )

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"


class Standup(BaseModel):
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        help_text="Team this standup belongs to"
    )
    start_time = models.TimeField(
        help_text="Time when standup starts (HH:MM)"
    )
    finish_time = models.TimeField(
        help_text="Time when standup finishes (HH:MM)"
    )
    schedule = models.IntegerField(
        default=0,
        help_text="Bitwise field for days of the week (will be implemented later)"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Is this standup schedule active?"
    )

    class Meta:
        verbose_name = 'Standup'
        verbose_name_plural = 'Standups'

    def __str__(self):
        return f"{self.team.name} Standup ({self.start_time}-{self.finish_time})"


class StandupQuestion(BaseModel):
    standup = models.ForeignKey(
        'Standup',
        on_delete=models.CASCADE,
        help_text="Standup this question belongs to"
    )
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        help_text="Question included in this standup"
    )
    order = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Order of this question within the standup (uses question order if not set)"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Is this question active in this standup?"
    )

    class Meta:
        verbose_name = 'Standup Question'
        verbose_name_plural = 'Standup Questions'
        unique_together = ['standup', 'question']
        ordering = ['standup', 'order']

    @property
    def question_order(self):
        return self.order if self.order is not None else self.question.order

    def __str__(self):
        return f"{self.standup.team.name} - {self.question.title}"


class Session(BaseModel):
    standup = models.ForeignKey(
        'Standup',
        on_delete=models.CASCADE,
        help_text="Standup this session belongs to"
    )
    started_at = models.DateTimeField(
        help_text="When the standup session started"
    )
    finished_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the standup session finished"
    )
    discord_message_id = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Discord message ID for this session"
    )

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'
        ordering = ['-started_at']

    def __str__(self):
        return f"{self.standup.team.name} Session - {self.started_at.strftime('%Y-%m-%d %H:%M')}"


class SessionMember(BaseModel):
    session = models.ForeignKey(
        'Session',
        on_delete=models.CASCADE,
        help_text="Session this member participation belongs to"
    )
    team_member = models.ForeignKey(
        'TeamMember',
        on_delete=models.CASCADE,
        help_text="Team member participating in this session"
    )
    finished_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When this member finished their standup"
    )
    discord_message_id = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Discord message ID for this session member"
    )

    class Meta:
        verbose_name = 'Session Member'
        verbose_name_plural = 'Session Members'
        unique_together = ['session', 'team_member']
        ordering = ['session', 'team_member']

    def __str__(self):
        return f"{self.session.standup.team.name} - {self.team_member.name}"


class SessionMemberAnswer(BaseModel):
    session_member = models.ForeignKey(
        'SessionMember',
        on_delete=models.CASCADE,
        help_text="Session member this answer belongs to"
    )
    standup_question = models.ForeignKey(
        'StandupQuestion',
        on_delete=models.CASCADE,
        help_text="Standup question being answered"
    )
    value = models.TextField(
        help_text="Answer content"
    )

    class Meta:
        verbose_name = 'Session Member Answer'
        verbose_name_plural = 'Session Member Answers'
        unique_together = ['session_member', 'standup_question']
        ordering = ['session_member', 'standup_question']

    def __str__(self):
        return f"{self.session_member.team_member.name} - {self.standup_question.question.title}"
