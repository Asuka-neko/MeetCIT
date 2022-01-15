from django.forms import ModelForm, DateInput
from django.utils import timezone
from cal.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = ['zoom_link', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean(self):
        super(EventForm, self).clean()

        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        if (start_time > end_time):
            self._errors['start_time'] = self.error_class(
                ['Start time cannot be later than end time!'])
        if (start_time <= timezone.now):
            self._errors['start_time'] = self.error_class(
                ['Start time cannot be earlier than current time!'])
        if (end_time <= timezone.now):
            self._errors['end_time'] = self.error_class(
                ['End time cannot be earlier than current time!'])

        return self.cleaned_data
