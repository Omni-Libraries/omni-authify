# Installation Guide

Omni-Authify is a Python library that makes it easy to add OAuth2 authentication to your applications. This documentation will guide you through installation, usage, and configuration.

## 📚 Table of Contents
- [Usage Guides](usage)
- [Supported Providers](providers.md)
- [Contributing](../CONTRIBUTING.md)
- [License](../LICENSE)

---
## 📦 Installation Options 🛠️ 

**Basic Installation**:

Install Omni-Authify using pip:

```bash
pip install omni-authify[django] # for Django based projects
```
```bash
pip install omni-authify[drf] # for Django Rest framework base project
```
```shell
pip install omni-authify[fastapi] # for FastAPI based projects
```
```shell
pip install omni-authify[flask] # for Flask based projects
```

# 📋 Requirements

* **Python 3.8+**
* **pip 24.3.1+**

## 🔗 Dependencies

* **requests**: `requests>=2.32.3`

## 🧩 Framework-Specific Dependencies

### Django Support
* **Django**: `Django>=4.2, <=5.1.3`
* **Django REST Framework**: `djangorestframework>=3.12.3, <=3.15.2`

### Web Framework Support
* **Flask**: `Flask>=3.0.0`
* **FastAPI**: `fastapi>=0.115.0`

---

## 🚀 Usage Guides

Omni-Authify supports multiple providers, including Facebook, Instagram, and Google. 
Each provider requires specific credentials to get started.

### ⚙️ Provider Configuration
```python
# settings.py

import os 
from dotenv import load_dotenv

load_dotenv()


OMNI_AUTHIFY = {
    'PROVIDERS': {
        'facebook': {
            'client_id': os.getenv('FACEBOOK_CLIENT_ID'),
            'client_secret': os.getenv('FACEBOOK_CLIENT_SECRET'),
            'redirect_uri': os.getenv('FACEBOOK_REDIRECT_URI'),
            'state': os.getenv('FACEBOOK_STATE'), # optional
            'scope': os.getenv('FACEBOOK_SCOPE'), # by default | add other FB app permissions you have!
            'fields': os.getenv('FACEBOOK_FIELDS'),
        },
        'github':{
            'client_id':os.getenv('GITHUB_CLIENT_ID'),
            'client_secret':os.getenv('GITHUB_CLIENT_SECRET'),
            'redirect_uri':os.getenv('GITHUB_REDIRECT_URI'),
            'state': os.getenv('GITHUB_STATE'),
            'scope':os.getenv('GITHUB_SCOPE'),
        },
        'google': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
            'redirect_uri': os.getenv('GOOGLE_REDIRECT_URI'),
            'state': os.getenv('GOOGLE_STATE'), # optional
            'scope': os.getenv('GOOGLE_SCOPES'),
        },
        'linkedin': {
            'client_id': os.getenv('LINKEDIN_CLIENT_ID'),
            'client_secret': os.getenv('LINKEDIN_CLIENT_SECRET'),
            'redirect_uri': os.getenv('LINKEDIN_REDIRECT_URI'),
            'scope': os.getenv('LINKEDIN_SCOPE'),
        },
                
        # Add other providers here if needed
        'telegram': {
            # Coming....
        }
    }
}
```

#### 🌟 [More Provider Configurations Coming Soon...]

---

## 📜 License

Omni-Authify is licensed under the MIT License. See the [LICENSE file](../LICENSE) for details.

---

Omni-Authify makes adding OAuth2 authentication to your project a breeze. Follow the instructions above to integrate social logins into your app quickly and efficiently!

