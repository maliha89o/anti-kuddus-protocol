from django.db import models

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20, unique=True)
    height_cm = models.PositiveIntegerField()
    needs_front_row = models.BooleanField(
        default=False,
        help_text="Vision/hearing impairment thakle True koro - height niye bepar na kore front e boshbe"
    )

    def __str__(self):
        return f"{self.name} ({self.roll}) - {self.height_cm}cm"


class ClassroomLayout(models.Model):
    """Ekta classroom er grid structure - kotto row, kotto column"""
    name = models.CharField(max_length=50, default="Section B")
    rows = models.PositiveIntegerField(default=6)
    columns = models.PositiveIntegerField(default=5)
    aisle_after_column = models.PositiveIntegerField(
        default=0,
        help_text="Center aisle kon column er por - 0 hole aisle nai"
    )

    def __str__(self):
        return f"{self.name} ({self.rows}x{self.columns})"


class SeatAssignment(models.Model):
    layout = models.ForeignKey(ClassroomLayout, on_delete=models.CASCADE, related_name='assignments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()

    class Meta:
        unique_together = ('layout', 'row', 'column')

    def __str__(self):
        return f"{self.student.name} - Row {self.row}, Col {self.column}"
