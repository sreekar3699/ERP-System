# ERP System

A Django-based enterprise resource planning application for managing users, customers, products, categories, subscriptions, and payments.

## Features

- User registration, login, verification, logout, and password reset flows
- Separate customer and administrator experiences
- Product and category management
- Customer and profile management
- Subscription pricing and premium access
- Razorpay payment integration
- Media uploads and static assets
- Django administration interface

## Technology

- Python 3.10+
- Django 4.x
- MySQL
- HTML, CSS, and JavaScript
- Razorpay for payment processing

## Project Structure

```text
ERP/
├── accounts/      # Authentication and account workflows
├── adminapp/      # ERP administration, products, customers, and payments
├── ERP/           # Django project configuration and root URL routing
├── templates/     # Shared application templates
├── static/        # CSS, JavaScript, and images
├── media/         # Uploaded media
└── manage.py      # Django management entry point
```

## Getting Started

1. Clone the repository and enter the project directory.
2. Create and activate a virtual environment:

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. Install the project dependencies. At minimum, install Django and the MySQL driver required by your environment.
4. Configure the database, email, payment, and host settings for your local environment. Do not commit passwords, API keys, or other secrets.
5. Apply migrations:

	```bash
	python manage.py migrate
	```

6. Start the development server:

	```bash
	python manage.py runserver
	```

Open `http://127.0.0.1:8000/` in a browser.

## Common URLs

- `/register` - Create an account
- `/login` - Sign in
- `/admin/` - Django administration
- `/adminhome` - ERP administrator dashboard
- `/allProducts` - Product management
- `/allCustomers` - Customer management
- `/pricing` - Subscription pricing

## Security Notes

Before deploying, set `DEBUG = False`, restrict `ALLOWED_HOSTS`, use environment variables for secrets, and configure production static and media storage.