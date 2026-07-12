from django.db import models


class SchoolRule(models.Model):
    """The 'Official School Rulebook' - source of truth for fact-checking."""
    rule_text = models.TextField(help_text="The actual, verbatim school rule")
    category = models.CharField(max_length=100, blank=True, help_text="e.g. Captain Duties, Homework, Discipline")

    def __str__(self):
        return self.rule_text[:60]