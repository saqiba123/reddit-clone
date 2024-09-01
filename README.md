# Reddit Clone
A basic Reddit clone application built with Django. This project demonstrates a social media platform where users can post, upvote, and comment on posts.

## Features

- User authentication (login, logout, registration)
- Create, edit, and delete posts
- Upvote and downvote posts
- Comment on posts
- View posts and comments on the homepage

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/reddit-clone.git
   cd reddit-clone
   ```
## Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
## Configure the Database

Edit yourprojectname/settings.py to set up the database. For SQLite:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```
## Apply Migrations

```bash
python manage.py migrate
```
## Create a Superuser
```bash
python manage.py createsuperuser
```
## Run the Development Server
```bash
python manage.py runserver
```
