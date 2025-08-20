# newsole2

A Django-based e-commerce app for selling limited edition shoes, featuring product browsing, wishlist management, and a shopping cart system.

## Features Summary

- **Product Listings** – Browse limited edition shoes.
- **Shopping Cart** – Add shoes for purchase.
- **Quantity Update** – Increase the quantity of a specific shoe in the cart by shoe ID.
- **Responsive Design** – Optimized for desktop and mobile.
- **Cloud Storage** – Images and files stored via Cloudinary.
- **PostgreSQL Database** – Reliable and scalable product storage.
- **Secure Authentication** – User accounts with login and signup functionality.

---

## Features

### 🏠 Home & Product Display

- **Home Page**: Displays a curated list of popular shoes.
- **Shoe List Page**: Shows all available shoes.
- **Shoe Detail Page**: Displays detailed shoe information with purchase and wishlist options.

### 🛒 Shopping Cart

- **Add to Cart**: Add shoes to the shopping cart.
- **Remove from Cart**: Remove selected shoes from the shopping cart.
- **View Cart**: Displays all items currently in the cart.

### ❤️ Wishlist

- **Add to Wishlist**: Save shoes to the wishlist for later consideration.
- **Remove from Wishlist**: Remove shoes from the wishlist.
- **Wishlist → Cart Transfer**: Move selected shoes from wishlist to cart.
- **Cart → Wishlist Transfer**: Move selected shoes from cart to wishlist.

### 📂 Data Management

- **Database Integration**: Uses Django ORM for managing shoe data.
- **Session-Based Storage**: Cart and wishlist data stored in Django sessions.

### 🖼 Image Hosting

- **Cloudinary Integration**: Stores and serves shoe images.

---

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Function-Based Views), Python
- **Database**: SQLite3 (local dev) / Render (production)
- **Media Storage**: Cloudinary
- **Version Control**: Git & GitHub
- **Deployment**: Render

---

## Setup & Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/newsole.git

# Navigate into the project folder
cd newsole

# Install dependencies
pipenv install

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

```

## File Structure

```
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
│        ├── **pycache**.py
│        ├── **init**.py
│        └─── seed_shoes.py # for seed content
│   ├──  migrations/
│   ├──  templates/
│        ├── about.html
│        ├── add_to_cart.html
│        ├── base.html # container
│        ├── breadcrumbs.html
│        ├── cart.html
│        ├── checkout.html
│        ├── contact.html
│        ├── footer.html
│        ├── header.html
│        ├── home.html
│        ├── login.html
│        ├── messages.html
│        ├── navbar.html
│        ├── shoe_detail.html # product detail page
│        ├── shoe_list.html # product listing page
│        ├── signup.html
│        ├── welcome_email.html
│        ├── wishlist.html
│        └─── **init**.py
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
│   ├── views.py
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

## Uses sqlite as database for local building

## Uses Postgres for production

## Start Postgres locally

Start PostgreSQL locally (macOS)
`brew services start postgresql`

Access PostgrSQL shell in local terminal:
`psql postgres`

Check if PostgreSQL is running
`brew services list`

## Test .env variables

`python manage.py shell`
