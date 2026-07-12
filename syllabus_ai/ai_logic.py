import json
from groq import Groq
from django.conf import settings
from .models import CurriculumTopic


def _get_client():
    return Groq(api_key=settings.LLM_API_KEY)


def summarize_syllabus(raw_text: str) -> str:
    """
    Baseline: Kuddus er lomba/terrifying syllabus text ke
    LLM diye clean bullet-point list e summarize kora.
    """
    client = _get_client()

    prompt = f"""Tumi ekta helpful assistant, jar kaj hocche student der
জন্য জটিল সিলেবাস কে সহজ bullet point list e summarize kora.

Nicher syllabus text ta poro, ar shudhu real, examinable topic gulo
niye ekta clean bullet-point list banaw. Kono explanation lagbe na,
shudhu bullet list.

Syllabus text:
\"\"\"{raw_text}\"\"\"

Output format: shudhu bullet points, Bangla ba English joto relevant hoy."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def filter_with_curriculum(raw_text: str) -> str:
    """
    Advanced (RAG): Official curriculum (CurriculumTopic table) context
    hisebe inject kore, Kuddus er fake/non-examinable content
    (jemon 'writer's biography', 'barcode') filter out kora.
    """
    client = _get_client()

    topics = CurriculumTopic.objects.filter(is_examinable=True)
    curriculum_context = "\n".join([f"- {t.chapter}: {t.topic}" for t in topics])

    if not curriculum_context:
        curriculum_context = "(Kono official curriculum data নেই এখনো, general judgement use koro)"

    prompt = f"""Tumi ekta strict curriculum checker. Nicher "Official Curriculum"
list ta holo ashol examinable topics. Ei list er against Kuddus er deya
syllabus statement ta check koro, ar shudhu segula bullet point e রাখো
যেগুলো official curriculum er sathe match kore. Non-examinable garbage
(jemon "writer's biography", "index", "barcode", ইত্যাদি) বাদ দাও।

Official Curriculum:
{curriculum_context}

Kuddus er Syllabus Statement:
\"\"\"{raw_text}\"\"\"

Output: shudhu filtered, examinable topic gulor bullet list."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def generate_study_plan(filtered_topics: str, days_remaining: int = 7) -> dict:
    """
    Advanced: filtered topics ke ekta structured JSON study plan e
    convert kora, {days_remaining} din er countdown schedule hisebe.
    """
    client = _get_client()

    prompt = f"""Nicher filtered topic list ta {days_remaining} diner
modhye study korar jonno ekta time-blocked JSON study plan banaw.

Topics:
{filtered_topics}

Output MUST be valid JSON only, no markdown, no explanation, in this exact format:
{{
  "total_days": {days_remaining},
  "schedule": [
    {{"day": 1, "topics": ["topic1", "topic2"], "focus": "short description"}},
    {{"day": 2, "topics": ["topic3"], "focus": "short description"}}
  ]
}}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.choices[0].message.content.strip()

    # Groq majhe majhe ```json ... ``` wrap kore dey, oita clean kori
    if text.startswith('```'):
        text = text.split('```')[1]
        if text.startswith('json'):
            text = text[4:]
        text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"error": "AI response valid JSON na, raw text:", "raw": text}