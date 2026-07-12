from django.db import models


class SOSAlert(models.Model):
    LOCATION_CHOICES = [
        ('library', 'Library'),
        ('playground', 'Playground'),
        ('corridor', 'Corridor'),
        ('classroom', 'Classroom'),
        ('canteen', 'Canteen'),
    ]

    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    triggered_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False, help_text="Captain marks true once handled")
    synced_from_offline = models.BooleanField(default=False, help_text="True if this was queued offline and synced later")

    def __str__(self):
        return f"SOS at {self.get_location_display()} - {self.triggered_at.strftime('%d %b %Y %H:%M')}"

    class Meta:
        ordering = ['-triggered_at']