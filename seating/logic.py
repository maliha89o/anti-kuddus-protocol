def generate_seating(students, rows, columns):
    """
    Baseline: height onujayi front theke back e sorting.
    needs_front_row=True hole height ignore kore front row e boshabe.

    students: Student queryset/list
    Return: dict {(row, col): student}
    """
    students = list(students)

    # Step 1: Priority students (impairment) - eder age front row e boshai
    priority = [s for s in students if s.needs_front_row]
    normal = [s for s in students if not s.needs_front_row]

    # Normal students height onujayi sort - choto age (front row e), lomba pichhone
    normal.sort(key=lambda s: s.height_cm)

    # Priority + normal - priority ra shobar age boshbe (front-most)
    ordered = priority + normal

    seating = {}
    total_seats = rows * columns

    for idx, student in enumerate(ordered[:total_seats]):
        row = idx // columns  # 0-indexed row (0 = front row)
        col = idx % columns
        seating[(row, col)] = student

    return seating


def check_line_of_sight(seating, rows, columns, target_row, target_col, teacher_row=-1):
    """
    Advanced: Teacher (podium, generally row -1 / front-center) theke
    Kuddus er seat (target_row, target_col) porjonto clear view ache kina check kore.

    Logic: target_col er same column e, target_row er age (upore/front e)
    boshe thaka shob student er height sum kore dekhi kuddus er dekha
    jabe kina block hoye. Simple heuristic: jodi kono age-boshe-thaka
    student er height kuddus er nijer height theke onek beshi hoy, তাহলে
    blocked dhori (cumulative obstruction model).

    Return: dict with 'blocked': bool, 'blocking_students': list
    """
    blocking_students = []
    kuddus = seating.get((target_row, target_col))

    if not kuddus:
        return {'blocked': False, 'blocking_students': [], 'reason': 'Kuddus er seat khuje paini'}

    kuddus_height = kuddus.height_cm

    # Same column e, target_row er age (samne) boshe thaka students check kori
    for r in range(0, target_row):
        seat = seating.get((r, target_col))
        if seat and seat.height_cm > kuddus_height + 15:
            # 15cm+ lomba hole shishe teacher er view block korte pare
            blocking_students.append(seat)

    return {
        'blocked': len(blocking_students) > 0,
        'blocking_students': blocking_students,
        'kuddus': kuddus,
    }