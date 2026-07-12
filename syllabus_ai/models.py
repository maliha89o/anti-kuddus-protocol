from django.db import models

from django.db import models


class SyllabusRequest(models.Model):
    raw_text = models.TextField(help_text="Kuddus er original syllabus statement")
    filtered_topics = models.TextField(blank=True, help_text="AI diye clean kora bullet list")
    study_plan_json = models.TextField(blank=True, help_text="Structured JSON study plan")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request #{self.id} - {self.created_at.strftime('%d %b %Y')}"


class CurriculumTopic(models.Model):
    """RAG er jonno: official curriculum, Kuddus er fake content filter korte."""
    chapter = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    is_examinable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.chapter}: {self.topic}"
