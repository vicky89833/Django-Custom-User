# Django Custom User
 
Here's a sample `README.md` file for a Django project using a custom user model. You can adjust it based on your project's specifics:

---

# Django Custom User Model

This repository provides a Django project template with a custom user model. Custom user models are useful when you need to add additional fields or change the authentication model of your Django application.

## Features

- Custom user model with additional fields.
- Custom `UserManager` for managing user creation.
- `AbstractBaseUser` and `PermissionsMixin` integration.
- Example `User` registration and authentication.
- Admin integration for managing custom users.
  
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-custom-user.git
   cd django-custom-user
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the admin interface:**

   Open your browser and go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Log in using the superuser credentials you created.

## Project Structure

```
django-custom-user/
│
├── user/                        # Example Django app
│   ├── migrations/               # Migration files for the app
│   ├── admin.py                  # Admin customization for custom user model
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Custom user model definition
│   ├── views.py                  # Example views using the custom user model
│   ├── serializers.py            # Custom user serializers for API usage
│   ├── urls.py                   # App-level URLs configuration
│   └── ...
│
├── core/
│   ├── settings.py               # Django project settings
│   ├── urls.py                   # Project-level URLs configuration
│   ├── wsgi.py                   # WSGI configuration for deployment
│   └── ...
│
├── manage.py                     # Django's command-line utility
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation (this file)
```

## Custom User Model

The custom user model is defined in `myapp/models.py` using `AbstractBaseUser` and `PermissionsMixin`. This model includes additional fields such as `date_of_birth` and `phone_number`, and it uses a custom manager (`UserManager`) to handle user creation and management.

### Model Overview

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
```

## Custom User Manager

The `UserManager` class is responsible for handling the creation of regular users and superusers. The `create_user` method handles setting the user's password and saving the user to the database, while `create_superuser` sets additional permissions required for admin access.

## Usage

- Use the custom user model in your applications by referring to it using `settings.AUTH_USER_MODEL`.
- Create new user instances using the custom manager (`UserManager`).

```python
from django.conf import settings
from myapp.models import User

# Create a new user
user = User.objects.create_user(email='user@example.com', password='password123', date_of_birth='1990-01-01')

# Create a new superuser
admin = User.objects.create_superuser(email='admin@example.com', password='adminpassword', date_of_birth='1985-05-05')
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Feel free to open an issue or submit a pull request if you have any suggestions or improvements.

## Contact

For any inquiries or issues, please contact [vicky.jnv898@gmail.com].

---

This template README includes an overview of the custom user model, installation instructions, project structure, and usage examples. Modify the sections as needed to match your project's specifics!
