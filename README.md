# Anti-Kuddus Protocol 🛡️

BAIUST CSE Spring Fest 2026 Hackathon Submission — "The Fall of Kodu Kuddus"

## Overview
A Django-based system to track and resolve student grievances against a
tyrannical Class Captain (Kodu Kuddus), built for the BAIUST Computer Club
Hackathon.

## Features Implemented

### Mission 1: Anonymous Whistleblower (Strike Generator)
- Roll-number based session verification
- Complaint submission form (category, description, evidence photo)
- Dynamic dashboard showing warnings progress (X/3)
- **Advanced**: EXIF metadata stripping on uploaded evidence photos
- **Advanced**: Roll numbers stored as one-way bcrypt hashes, never linked
  directly to complaints (anonymity pipeline)

### Mission 2: Anti-Camouflage Seat Planner
- Student record input (Name, Roll, Height)
- Dynamic N×M classroom grid UI
- Height-based ascending sort (front to back)
- **Advanced**: Line-of-sight algorithm checking teacher's view to Kuddus's desk
- **Advanced**: Priority handling for students needing front-row seating
  (vision/hearing impairments)

## Tech Stack
- Backend: Django 6.0.7
- Database: SQLite
- Image Processing: Pillow
- Hashing: bcrypt
- Frontend: Django Templates + custom CSS

## Setup Instructions

1. Clone the repository
```bash
   git clone <repo-url>
   cd anti_kuddus_protocol
```

2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file in the project root
5. Run migrations
```bash
   python manage.py migrate
```

6. Create a superuser (for admin access)
```bash
   python manage.py createsuperuser
```

7. Run the development server
```bash
   python manage.py runserver
```

8. Visit `http://127.0.0.1:8000/strikes/login/` for the complaint portal,
   `http://127.0.0.1:8000/seating/students/` for the seating planner, and
   `http://127.0.0.1:8000/admin/` for the admin panel.

## Architecture Notes

- **Apps**: `strikes` (Mission 1), `seating` (Mission 2)
- **Anonymity design**: The `Complaint` model has no foreign key to any
  student/roll-number table, so even a full database leak cannot link a
  complaint back to its author.
- **EXIF stripping**: Implemented via a `Complaint.save()` override that
  re-encodes uploaded images pixel-by-pixel using Pillow, discarding all
  metadata.
- **Seating algorithm**: Students needing front-row placement are seated
  first (row-major order), followed by remaining students sorted by
  ascending height, filling the grid row by row.

## Trade-offs
- SQLite used for simplicity/hackathon speed; would move to PostgreSQL
  for production.
- Line-of-sight uses a simplified cumulative-height heuristic rather than
  true geometric ray-casting, given the time constraints.

## Screenshots
(Add screenshots here before final submission)