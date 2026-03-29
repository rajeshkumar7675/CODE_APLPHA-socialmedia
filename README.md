# SocialHub – Mini Social Media App

A full-featured social media application built with **Django 2.2** (Python 3.7 compatible),
vanilla HTML/CSS/JavaScript for the frontend, and SQLite as the database.

---

## Features

| Feature | Description |
|---|---|
| **User Auth** | Register, login, logout with Django's built-in auth |
| **User Profiles** | Avatar, bio, location, website, join date |
| **Posts** | Create, view, delete posts with optional image upload |
| **Comments** | AJAX-powered inline comments on every post |
| **Likes** | One-click AJAX like/unlike with live count update |
| **Follow System** | Follow/unfollow users with live follower count |
| **Feed** | Personalised feed showing posts from followed users |
| **Explore** | Search posts and people by keyword |
| **Admin Panel** | Django admin for all models |

---

## Project Structure

```
socialmedia/
├── manage.py
├── requirements.txt
├── setup_and_run.sh          ← one-command setup
├── db.sqlite3                ← auto-created on first run
├── media/                    ← uploaded images
│   └── avatars/
├── socialmedia/              ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                     ← main application
    ├── models.py             ← Profile, Post, Comment, Like, Follow
    ├── views.py              ← all view logic
    ├── urls.py               ← URL routing
    ├── forms.py              ← Django forms
    ├── admin.py              ← admin registration
    ├── signals.py            ← auto-create Profile on User creation
    ├── apps.py
    ├── templates/core/
    │   ├── base.html
    │   ├── login.html
    │   ├── register.html
    │   ├── home.html
    │   ├── explore.html
    │   ├── profile.html
    │   ├── edit_profile.html
    │   ├── post_card.html    ← reusable post component
    │   ├── post_detail.html
    │   └── confirm_delete.html
    └── static/core/
        ├── css/style.css
        └── js/main.js
```

---

## Quick Start

### Option A – One command (Linux / macOS)

```bash
cd socialmedia
chmod +x setup_and_run.sh
./setup_and_run.sh
```

### Option B – Manual steps

```bash
# 1. Go into the project folder
cd socialmedia

# 2. Create & activate a virtual environment
python3.7 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations core
python manage.py migrate

# 5. (Optional) Create a superuser for the admin panel
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

---

## Database Models

```
User (Django built-in)
 └─ Profile         (1-to-1)   avatar, bio, location, website
 └─ Post            (1-to-many) content, image, created_at
     └─ Comment     (1-to-many) content, author, created_at
     └─ Like        (many-to-many via through) user, post
 └─ Follow          (self-referential) follower, following
```

---

## URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `home_view` | Personalised feed |
| `/register/` | `register_view` | Sign up |
| `/login/` | `login_view` | Sign in |
| `/logout/` | `logout_view` | Sign out |
| `/explore/` | `explore_view` | Explore & search |
| `/profile/<username>/` | `profile_view` | User profile |
| `/profile/edit/me/` | `edit_profile_view` | Edit own profile |
| `/post/<id>/` | `post_detail_view` | Post + all comments |
| `/post/<id>/delete/` | `delete_post_view` | Delete own post |
| `/post/<id>/like/` | `toggle_like_view` | AJAX like/unlike |
| `/post/<id>/comment/` | `add_comment_ajax` | AJAX add comment |
| `/follow/<username>/` | `toggle_follow_view` | AJAX follow/unfollow |
| `/admin/` | Django admin | Admin panel |

---

## Python 3.7 Compatibility

This project deliberately uses:
- **Django 2.2 LTS** — the last LTS release that supports Python 3.7
- **Pillow 8.4.0** — last version with Python 3.7 wheels on PyPI
- No f-strings from Python 3.8+ (walrus operator `:=`, etc.)
- `str.format()` and `%`-formatting throughout the codebase
- `os.path.join()` instead of `pathlib` (3.6+ but more cautious)

---

## Tech Stack

- **Backend**: Python 3.7 / Django 2.2
- **Frontend**: HTML5, CSS3 (custom, no frameworks), vanilla JavaScript (ES6 fetch API)
- **Database**: SQLite (zero config, swappable to PostgreSQL via `settings.py`)
- **Image Storage**: Local filesystem via Django's `MEDIA_ROOT`
