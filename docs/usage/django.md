# Django Integration for Facebook Authentication

Easily integrate Facebook OAuth2 authentication into your Django project using Omni-Authify. This guide covers configuration, view creation, URL setup, and handling user authentication, providing a seamless experience for developers.

---

## ⚙️ Configure Settings

Add the Omni-Authify settings to your Django project settings to include Facebook and/or any other OAuth providers.

```python
import os

OMNI_AUTHIFY = {
    'HOME_PAGE': {
        'dashboard': {
            'home': 'the-page_name-where-you-redirect-the-user-after-authentication-and-login'
        }
    },
    'PROVIDERS': {
        'facebook': {
            'client_id': os.getenv('FACEBOOK_CLIENT_ID'),
            'client_secret': os.getenv('FACEBOOK_CLIENT_SECRET'),
            'redirect_uri': '🌐http://localhost:8000/facebook/callback',
            'state': 'your-unguessable-state', # optional
            'fields': 'id,name,email,picture...'
        },
        # Add other providers here if needed
    }
}
```

---

## Django Views

Learn how to create views to handle Facebook login and callback in your Django application.

### 📝 Prerequisites

- **Django 2.2 or higher**
- Omni-Authify installed and configured (see [Installation Guide](../installation.md))

### 🚀 Setting Up Views

Create views to handle the login and callback processes.

#### **views.py**

```python
from django.shortcuts import redirect, render
from django.http import HttpResponse
from omni_authify.providers import Facebook

import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the provider with environment variables
facebook_provider = Facebook(
    client_id=os.getenv('FACEBOOK_CLIENT_ID'),
    client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
    redirect_uri=os.getenv('FACEBOOK_REDIRECT_URI')
)

def facebook_login(request):
    # Generate authorization URL and redirect the user
    auth_url = facebook_provider.get_authorization_url(state='your_random_state')
    return redirect(auth_url)

def facebook_callback(request):
    # Handle the callback from Facebook
    error = request.GET.get('error')
    if error:
        return HttpResponse(f"Error: {error}", status=400)
    
    code = request.GET.get('code')
    if not code:
        return HttpResponse("No code provided", status=400)
    
    try:
        # Exchange code for access token
        access_token = facebook_provider.get_access_token(code)
        # Fetch user profile
        user_info = facebook_provider.get_user_profile(access_token)
        # TODO: Authenticate the user in your application
        return render(request, 'home.html', {'user_info': user_info})
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
```

---

### 🔁 Alternative Implementation

#### **views.py (Alternative Approach)**

This version leverages the OmniAuthifyDjango helper class for a simpler implementation.

```python
from omni_authify import OmniAuthifyDjango

def facebook_login(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    return auth.login(request)

def facebook_callback(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    # Todo: Authenticate/login the user and save the user_info on your own!
    return auth.callback(request)
```

---

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

