from django.db import models

# Create your models here.



class Category(models.Model):
    """Event category (e.g. Conference, Workshop)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]                # alphabetical
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    """Single scheduled event."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="events",
    )

    class Meta:
        ordering = ["-date", "time"]       # newest first
        indexes = [
            models.Index(fields=["date"]),
            models.Index(fields=["category", "date"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} ({self.date})"


class Participant(models.Model):
    """Person who can attend multiple events."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    events = models.ManyToManyField(
        Event,
        related_name="participants",
        blank=True,
    )

    class Meta:
        unique_together = ("name", "email")   # prevent exact duplicates
        ordering = ["name"]
        indexes = [models.Index(fields=["email"])]

    def __str__(self) -> str:
        return self.name
