# Anti-Kuddus Protocol 🛡️

BAIUST CSE Spring Fest 2026 Hackathon Submission — "The Fall of Kodu Kuddus"

## Overview

A Django-based system to organize students, track the tyranny of a corrupt
Class Captain (Kodu Kuddus), and safely deliver the three strikes needed
for his impeachment. Built for the BAIUST Computer Club Hackathon (Senior
Track — all Baseline and Advanced Engineering requirements implemented).

## Features Implemented

### Core: Authentication & Central Dashboard
- Landing page with Login / Sign Up
- Django's built-in auth system (session-based)
- Central dashboard with sidebar navigation and card-based access to all
  six missions

### Mission 1: Anonymous Whistleblower (Strike Generator)
- Roll-number based session verification
- Complaint submission form (category, description, evidence photo)
- Dynamic dashboard showing warnings progress (X/3) with an impeachment
  progress bar
- **Advanced — Absolute Anonymity Pipeline**: Roll numbers are hashed with
  bcrypt and never stored as a foreign key on the `Complaint` model, so a
  full database leak cannot link any complaint back to its author.
- **Advanced — Evidence Metadata Stripping**: Uploaded evidence photos are
  re-encoded pixel-by-pixel via Pillow on save, discarding all EXIF data
  (timestamps, GPS, camera signatures).

### Mission 2: Anti-Camouflage Seat Planner
- Student record input (Name, Roll, Height) via the admin panel
- Dynamic N×M classroom grid UI
- Height-based ascending sort (front row to back row)
- **Advanced — Line-of-Sight Optimization**: Calculates whether the
  teacher's podium has a clear view of Kuddus's desk, factoring in the
  height of students seated in front of him.
- **Advanced — Dynamic Constraints**: Students flagged with
  `needs_front_row` (vision/hearing impairments) are always seated in the
  front row regardless of height.

### Mission 3: Syllabus Negotiator (AI Integration)
- Text input for Kuddus's long-form syllabus statements
- LLM integration (Groq API, `llama-3.3-70b-versatile`) to summarize into
  a clean bulleted list
- **Advanced — Contextual RAG**: The official curriculum (`CurriculumTopic`
  table) is injected into the prompt context, so the AI cross-references
  Kuddus's syllabus against real, examinable topics and filters out
  non-examinable garbage (e.g. "writer's biography", "barcode").
- **Advanced — Smart Study Plan Generator**: Outputs a structured,
  time-blocked JSON study plan mapped to a countdown of days before the
  test.

### Mission 4: Corrupt Economy & Tiffin Ledger
- Anonymous transaction ledger for logging forced cash payments (washroom
  toll) and stolen food items
- Dashboard with running totals for cash extorted and food stolen
- **Advanced — Caloric vs. Kinetic Disparity Engine**: Tracks Kuddus's
  estimated caloric intake from stolen food against his energy expenditure
  (modeled as zero, given his indoor Ludu lifestyle).
- **Advanced — Projected Weaponry Conversions**: Converts total extorted
  cash in real time into relatable units (international-standard cricket
  bats, packets of premium jhalmuri).

### Mission 5: SOS Rescue Flare
- Mobile-friendly SOS button with a hardcoded location dropdown (Library,
  Playground, Corridor, Classroom, Canteen)
- Captain-facing dashboard showing active distress signals
- **Advanced — Real-Time Event Broadcast**: The captain dashboard polls
  the server every 3 seconds for new alerts, giving a near-real-time feed
  without requiring a full page refresh.
- **Advanced — Simulated Network Resilience**: If the student is offline
  when pressing SOS, the alert is queued in the browser's `localStorage`
  and automatically synced to the server once the connection returns
  (`window.addEventListener('online', ...)`).

### Mission 6: Kuddus Fact-Checker
- Text input for claims made by Kuddus
- **Advanced — Semantic Fact-Checking Engine**: Uses
  `sentence-transformers` (`all-MiniLM-L6-v2`) to embed both the claim and
  every rule in the `SchoolRule` table, then finds the closest match via
  cosine similarity — this is true semantic search, not simple string
  matching.
- **Advanced — Confidence Scoring**: Outputs a styled validation card with
  a bold TRUE/FALSE badge, a numeric confidence score, and the exact
  matched rule text to debunk (or confirm) the claim on the spot.

## Tech Stack

- **Backend**: Django 6.0.7
- **Database**: SQLite
- **AI/LLM**: Groq API (`llama-3.3-70b-versatile`)
- **Semantic Search**: sentence-transformers, scikit-learn (cosine
  similarity)
- **Image Processing**: Pillow (EXIF stripping)
- **Hashing**: bcrypt
- **Frontend**: Django Templates + vanilla CSS + vanilla JavaScript
  (fetch API for polling and offline queueing)

## Project Structure

```
anti_kuddus_protocol/
├── core/           # Landing page, auth (signup/login/logout), dashboard
├── strikes/        # Mission 1: Anonymous Whistleblower
├── seating/        # Mission 2: Anti-Camouflage Seat Planner
├── syllabus_ai/    # Mission 3: Syllabus Negotiator
├── economy/        # Mission 4: Corrupt Economy & Tiffin Ledger
├── sos/            # Mission 5: SOS Rescue Flare
├── factcheck/      # Mission 6: Kuddus Fact-Checker
├── accounts/       # (reserved for future auth extensions)
├── anti_kuddus/    # Project settings, root urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/maliha89o/anti-kuddus-protocol.git
   cd anti-kuddus-protocol
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root**
   ```
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   LLM_API_KEY=your-groq-api-key
   ```
   - Generate a Django secret key:
     ```bash
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
   - Get a free Groq API key at [console.groq.com](https://console.groq.com)

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Seed some data via the admin panel** (`/admin/`)
   - Add `Student` records for the Seating Planner
   - Add `CurriculumTopic` records for the Syllabus Negotiator's RAG filter
   - Add `SchoolRule` records for the Fact-Checker

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Visit the app**
   - `http://127.0.0.1:8000/` — Landing page (Login / Sign Up)
   - `http://127.0.0.1:8000/dashboard/` — Central dashboard (after login)
   - `http://127.0.0.1:8000/admin/` — Admin panel

## Architecture Notes

- **Anonymity design (M1)**: The `Complaint` model has no foreign key to
  any student/roll-number table, so even a full database leak cannot link
  a complaint back to its author. Roll numbers are only used transiently
  in the session during verification.
- **EXIF stripping (M1)**: Implemented via a `Complaint.save()` override
  that re-encodes uploaded images pixel-by-pixel using Pillow, discarding
  all metadata.
- **Seating algorithm (M2)**: Students needing front-row placement are
  seated first, followed by remaining students sorted by ascending
  height, filling the grid row by row. Line-of-sight is checked with a
  cumulative-height heuristic against the teacher's podium.
- **RAG for Syllabus AI (M3)**: Curriculum topics from the database are
  serialized into the LLM prompt as context, letting the model
  cross-reference and filter Kuddus's claims against real, examinable
  material.
- **Offline resilience (M5)**: The SOS trigger page listens for
  `online`/`offline` browser events. Alerts created while offline are
  queued in `localStorage` and flushed to the server automatically once
  connectivity is restored.
- **Semantic search (M6)**: Both the claim and all rules are embedded
  with the same sentence-transformer model; the rule with the highest
  cosine similarity is returned along with a confidence percentage.

## Trade-offs

- SQLite is used for simplicity and hackathon speed; a production
  deployment would move to PostgreSQL.
- Mission 5's "real-time" broadcast uses AJAX polling (every 3 seconds)
  rather than WebSockets/Django Channels, prioritizing reliability and
  implementation speed within the hackathon timeframe.
- Mission 2's line-of-sight check uses a simplified cumulative-height
  heuristic rather than true geometric ray-casting.
- Mission 6's TRUE/FALSE decision is threshold-based on semantic
  similarity to the closest rule; a production system would ideally use a
  second LLM pass to explicitly check for contradiction vs. agreement.

## Screenshots

*(Add screenshots of the dashboard, seating grid, syllabus AI output,
economy dashboard, SOS flow, and fact-checker result here before final
submission.)*

## Team

- Maliha Hossain — BAIUST CSE, Level 3 Term 1