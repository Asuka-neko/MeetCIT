from django.db import models
from django.urls import reverse


class Event(models.Model):
    mentor = models.CharField(max_length=200)
    zoom_link = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        permissions = (
            ('can_edit', 'Can edit the event'),
        )

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.mentor} </a>'
