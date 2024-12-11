# Django Integration for Facebook Login

Easily integrate Facebook OAuth2 authentication into your Django project using Omni-Authify. This guide covers configuration, view creation, URL setup, and handling user authentication, providing a seamless experience for developers.

---

## ⚙️ Configure Settings

Add the Omni-Authify settings to your Django project settings to include Facebook and/or any other OAuth providers.

```python
import os
from dotenv import load_dotenv

load_dotenv()

OMNI_AUTHIFY = {
    'PROVIDERS': {
        'facebook': {
            'client_id': os.getenv('FACEBOOK_CLIENT_ID'),
            'client_secret': os.getenv('FACEBOOK_CLIENT_SECRET'),
            'redirect_uri': os.getenv('FACEBOOK_REDIRECT_URI'),
            'state': 'you-super-state', # optional
            'scope': 'email,public_profile', # by default | add other FB app permissions you have!
            'fields': 'id,name,email,picture',
        },
                
        # Add other providers here if needed
        'google': {
            # Coming....
        }
    }
}

# Note: email and public_profile permissions is granted by default
#       if you want any other fields, you need to pass Facebook App Review. 
#       You can get those user info when fields are set to email and public_info:
#               User Info: {'id': '12212964..........', 'name': "Name Surname", 'email': 'user@example.com'}
```

---

## Django Views

Learn how to create views to handle Facebook login and callback in your Django application.

### 📝 Prerequisites

- **Installation**: Install Omni-Authify with Django support using the following command:

  ```bash
  pip install omni-authify[django]
  ```

- **Django 4.2 or higher**
- Omni-Authify installed and configured (see [Installation Guide](../installation.md))

### 🚀 Setting Up Views

Create class based views to handle the login and callback processes.

## 🔁 **views.py**

This version leverages the OmniAuthifyDjango helper class for a simpler implementation over function based views!.

```python
from django.http import HttpResponse
from omni_authify.frameworks.django import OmniAuthifyDjango

def facebook_login(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    return auth.login(request)

def facebook_callback(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    user_info = auth.callback(request)
    print(f"User info from Facebook: {user_info}")
    
     # Todo: Authenticate/login the user and save the user_info on your own!
    return HttpResponse(user_info)

```

## 🌐 Update URLs

Add the login and callback views to your app's **urls.py** file:

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('facebook/login/', views.facebook_login, name='facebook_login'),
    path('facebook/callback/', views.facebook_callback, name='facebook_callback'),
]
```

---

## 📄 Templates

Create a template to display user information or login options.

**home.html**

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
</head>
<body>
    {% if user_info %}
        <h1>Welcome, {{ user_info.name }}!</h1>
        <img src="{{ user_info.picture.data.url }}" alt="Profile Picture">
        <p>Email: {{ user_info.email }}</p>
    {% else %}
        <h1>Welcome to Our Site</h1>
        <a href="{% url 'facebook_login' %}">Login with Facebook</a>
    {% endif %}
</body>
</html>
```

---

## ✅ Best Practices

- **🔒 Use Environment Variables**: Always use environment variables to store important information like `client_id` and `client_secret`. This helps keep your credentials safe 🛡️.
- **🔗 Match Redirect URI**: Make sure the `redirect_uri` is consistent between your Facebook App settings and your code to avoid errors 🚫.
- **⚠️ Error Handling**: Ensure all potential errors are handled to provide a smooth user experience 🐞.

---

**Omni-Authify** makes adding Facebook authentication to your Django app straightforward and secure. Follow these steps and best practices to provide your users with a seamless login experience. 🚀✨

