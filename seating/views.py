from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, ClassroomLayout, SeatAssignment
from .logic import generate_seating, check_line_of_sight


def student_list(request):
    students = Student.objects.all()
    return render(request, 'seating/student_list.html', {'students': students})


def generate_seating_view(request):
    layout, _ = ClassroomLayout.objects.get_or_create(
        name="Section B",
        defaults={'rows': 6, 'columns': 5, 'aisle_after_column': 2}
    )
    students = Student.objects.all()

    if not students.exists():
        messages.error(request, "Age Student add koro admin panel theke")
        return redirect('student_list')

    seating = generate_seating(students, layout.rows, layout.columns)

    # Purono assignment clear kore notun save kori
    SeatAssignment.objects.filter(layout=layout).delete()
    for (row, col), student in seating.items():
        SeatAssignment.objects.create(layout=layout, student=student, row=row, col=col) \
            if False else SeatAssignment.objects.create(layout=layout, student=student, row=row, column=col)

    # Kuddus khuje ber kori (roll diye - example: roll = 'KUDDUS01')
    kuddus_pos = None
    for (row, col), student in seating.items():
        if 'kuddus' in student.name.lower():
            kuddus_pos = (row, col)
            break

    sight_result = None
    if kuddus_pos:
        sight_result = check_line_of_sight(seating, layout.rows, layout.columns, kuddus_pos[0], kuddus_pos[1])

    context = {
        'layout': layout,
        'seating': seating,
        'rows_range': range(layout.rows),
        'cols_range': range(layout.columns),
        'sight_result': sight_result,
    }
    return render(request, 'seating/grid.html', context)
