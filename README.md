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
```

## File Structure

my_django_app/
├── accounts/ # User authentication app
│ ├── migrations/
│ ├── templates/
│ │ └── registration/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── core/ # Main business logic app
│ ├── migrations/
│ ├── templates/
│ │ └── home.html
│ │ └── about.html
│ │ └── contact.html
│ │ └── base.html
│ ├── filters.py
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── config/ # Django settings package
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── media/ # Uploaded media (Cloudinary in production)
├── staticfiles/ # Collected static files
├── .gitignore
├── manage.py
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt

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
