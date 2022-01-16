from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    mentor = models.CharField(max_length=200)
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    zoom_link = models.TextField()
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.mentor

    def __str__(self):
        return self.zoom_link

    def __datetime__(self):
        return self.start_time

    def __datetime__(self):
        return self.end_time

    def __bool__(self):
        return self.available

    def is_available(self) -> bool:
        return self.start_time > timezone.now() and self.available

    def has_started(self):
        return self.start_time <= timezone.now() <= self.end_time

    def has_ended(self):
        return self.end_time < timezone.now()

    class Meta:
        permissions = (
            ('can_edit', 'Can edit the event'),
            ('cannot_book', 'Cannot book the event')
        )

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        title = self.mentor + " (BOOKED!)"
        if self.is_available():
            return f'<a href="{url}"> {self.mentor} </a>'
        else:

            return f'<a href="{url}"> {title} </a>'
