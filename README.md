# newsole2

A Django-based e-commerce app for selling limited edition shoes, featuring product browsing, wishlist management, and a shopping cart system.

Update October 4 2025: Render's database free tier has expired. Created another free tier cause I'm broke. 😢

## Features Summary

- **Product Listings** – Browse limited edition shoes.
- **Shopping Cart** – Add shoes for purchase.
- **Quantity Update** – Increase the quantity of a specific shoe in the cart by shoe ID.
- **Responsive Design** – Optimized for desktop and mobile.
- **Cloud Storage** – Images and files stored via Cloudinary.
- **PostgreSQL Database** – Reliable and scalable product storage.
- **Secure Authentication** – User accounts with login and signup functionality.

---

## 🚀 Features

### 🛍️ Product Management

- Displays shoes with details: name, description, price, categories, stock status, and images.
- Dynamic **stock availability** logic to show if a shoe is in stock.
- Pagination for better navigation (shows 5 items at a time with a "Show More" button).

### 🔍 Search

- Search shoes by name.
- Displays search results on the shoe listing page.

### ❤️ Wishlist & Cart

- **Add to Wishlist:** Save favorite shoes.
- **Move to Cart from Wishlist:** If the shoe is in stock, it moves to the cart; otherwise, it stays in the wishlist.
- **Move to Wishlist from Cart:** Easily move items back to wishlist.
- **Delete from Cart:** Remove items with a single click.

### 🔑 User Authentication

- **Signup, Login, Logout** powered by Django's built-in authentication and `django-allauth`.
- Extended signup form with **first name and last name** fields.
- Access control: Shoe list, wishlist, and cart pages are restricted to logged-in users.
- Redirect guests to login or signup when attempting to access protected pages.

### 📧 Email Automation

- Sends a **welcome email** to users after successful signup.
- Uses **Gmail SMTP** for sending emails securely.

### 🗄️ Database

- Integrated **PostgreSQL** for production.
- Configured and deployed on **Render**.

### 🎨 Frontend

- Fully responsive design using **Bootstrap**.

### 🖼 Image Hosting

- **Cloudinary Integration**: Stores and serves shoe images.

---

## 🛠️ Tech Stack

| Category           | Technology                    |
| ------------------ | ----------------------------- |
| **Framework**      | Django (Function-Based Views) |
| **Database**       | PostgreSQL                    |
| **Email**          | Gmail SMTP                    |
| **Authentication** | Django Allauth                |
| **Image Storage**  | Cloudinary                    |
| **Deployment**     | Render                        |
| **CSS Framework**  | Bootstrap 5                   |

---

## Setup, Installation, & Debugging (Cheat sheet)

```bash
# Clone the repository
git clone https://github.com/yourusername/newsole.git

# Navigate into the project folder
cd newsole

# Install dependencies (assuming that there's existing packages saved in Pipfile)
pipenv install

# Install Django
pipenv install django

# Activate the virtual environment
pipenv shell

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver

# Update a package
open requirements.txt and add the package name
pip install -r requirements.txt

# Overwrite requirements.txt with exact version of installed packages
pip freeze > requirements.txt

# Create superuser
python manage.py createsuperuser

# Connect to psql locally
python manage.py dbshell

# Connect to Render PostgreSQL DB locally
python "<external url found in render dashboard>"

# Assuming that shoe data is already configured in management folder, run this coded to seed shoe data
python manage.py seed_shoes

# Start Postgres locally
Start PostgreSQL locally (macOS)
brew services start postgresql

Access PostgrSQL shell in local terminal:
psql postgres

Check if PostgreSQL is running
brew services list

## Test .env variables
python manage.py shell


```

## File Structure

```bash
my_django_app/
├── accounts/ # User authentication app
│   ├──  migrations/
│   ├──  **init**.py
│   ├──  admin.py
│   ├──  apps.py
│   ├──  models.py
│   ├──  tests.py
│   └─── views.py
├── core/ # Main business logic app
│   ├──  **pycache**.py
│   ├──  management/
│   │    ├── **pycache**.py
│   │    ├── **init**.py
│   │    └─── seed_shoes.py # for seed content
│   ├──  migrations/
│   ├──  templates/
│   │    ├── about.html
│   │    ├── add_to_cart.html
│   │    ├── base.html # container
│   │    ├── breadcrumbs.html
│   │    ├── cart.html
│   │    ├── checkout.html
│   │    ├── contact.html
│   │    ├── footer.html
│   │    ├── header.html
│   │    ├── home.html
│   │    ├── login.html
│   │    ├── messages.html
│   │    ├── navbar.html
│   │    ├── shoe_detail.html # product detail page
│   │    ├── shoe_list.html # product listing page
│   │    ├── signup.html
│   │    ├── welcome_email.html
│   │    ├── wishlist.html
│   │    └─── **init**.py
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── context.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── shoe_data.py # 20 shoes here
│   ├── test.py
│   ├── urls.py
│   ├── utils.py
│   └─── views.py
├── staticfiles
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── mydb
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
└─── requirements.txt

```

### Key Files

| File/Folder           | Description                                    |
| --------------------- | ---------------------------------------------- |
| models.py             | Shoe model with stock logic                    |
| views.py              | Business logic for cart, wishlist, search, etc |
| templates/            | HTML templates styled with Bootstrap           |
| context_processors.py | Shows cart item count globally                 |

---

## Uses sqlite as database for local building

## Uses Postgres for production

## User Authentication

https://docs.djangoproject.com/en/5.2/ref/contrib/auth/#django.contrib.auth.models.User.first_name
https://docs.allauth.org/en/latest/account/configuration.html
https://docs.allauth.org/en/dev/installation/quickstart.html

## Credits

Classmate's notes from 2020!!!

Chatgpt and Gemini

Youtube tutorials

Nike.com and Lovebonito.com for research
