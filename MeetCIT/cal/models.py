from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    mentor = models.CharField(max_length=200)
    zoom_link = models.TextField()
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return self.mentor

    def __str__(self):
        return self.zoom_link

    def __str__(self):
        return self.start_date

    def __str__(self):
        return self.end_date

    def is_available(self):
        return (self.start_date > timezone.now and self.available)

    def has_started(self):
        return (self.start_date <= timezone.now <= self.end_date)

    def has_ended(self):
        return (self.end_date < timezone.now)

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.mentor} </a>'
