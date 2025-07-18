# 🏠 PropertyHub

**PropertyHub** is a full-stack property rental platform connecting renters with owners directly — built using **Flutter (frontend)** and **Django REST Framework (backend)** with **PostgreSQL** for storage.

---

## ⚙️ Tech Stack

- 🔙 Backend: Django + Django REST Framework
- 📱 Frontend: Flutter
- 🗄️ Database: PostgreSQL
- ☁️ API: RESTful endpoints
- 🔒 Auth: Token or Session-based (TBD)

---

## 🚀 Features

- User Sign Up / Login (Renters and Owners)
- Property Listings (with photos, rent, type, etc.)
- Search by city, type, and price range
- Save requirements / preferences
- Owner-Renter review system

---

## 🏗️ Project Structure

```bash
PropertyHubProject/
├── propertyhub/          # Django app (models, views, serializers, etc.)
├── manage.py
├── db.sqlite3 (if using SQLite)
├── requirements.txt
├── Pipfile / Pipfile.lock
└── README.md
