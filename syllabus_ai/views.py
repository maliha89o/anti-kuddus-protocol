import json
from django.shortcuts import render
from django.contrib import messages
from .forms import SyllabusInputForm
from .models import SyllabusRequest
from .ai_logic import summarize_syllabus, filter_with_curriculum, generate_study_plan


def syllabus_negotiator(request):
    result = None
    study_plan = None

    if request.method == 'POST':
        form = SyllabusInputForm(request.POST)
        if form.is_valid():
            raw_text = form.cleaned_data['raw_text']
            days = form.cleaned_data['days_remaining']

            try:
                # Advanced: RAG-based filtering (curriculum-aware)
                filtered = filter_with_curriculum(raw_text)

                # Advanced: structured JSON study plan
                study_plan = generate_study_plan(filtered, days)

                # DB e save kori
                SyllabusRequest.objects.create(
                    raw_text=raw_text,
                    filtered_topics=filtered,
                    study_plan_json=json.dumps(study_plan)
                )

                result = filtered
                messages.success(request, "Syllabus process hoye geche!")
            except Exception as e:
                messages.error(request, f"AI call e error hoyeche: {str(e)}")
    else:
        form = SyllabusInputForm()

    return render(request, 'syllabus_ai/negotiator.html', {
        'form': form,
        'result': result,
        'study_plan': study_plan,
    })