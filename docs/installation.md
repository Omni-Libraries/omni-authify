# Installation Guide

Omni-Authify is a Python library that makes it easy to add OAuth2 authentication to your applications. This documentation will guide you through installation, usage, and configuration.

## 📚 Table of Contents
- [Usage Guides](usage)
- [Supported Providers](providers.md)
- [Contributing](../CONTRIBUTING.md)
- [License](../LICENSE)

---

## 🛠️ Installation Guide

### 🚀 Quick Start

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

### 📋 Requirements

- **Python 3.7+**
- **pip 24.3.1+**

### 🔗 Dependencies

- **requests**: `requests>=2.32.3`

---

## 🚀 Usage Guides

Omni-Authify supports multiple providers, including Facebook, Instagram, and Google. Each provider requires specific credentials to get started.

### ⚙️ Provider Configuration

#### Facebook/Instagram
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
```

#### 🌟 [More Provider Configurations Coming Soon...]

---

## 📜 License

Omni-Authify is licensed under the MIT License. See the [LICENSE file](../LICENSE) for details.

---

Omni-Authify makes adding OAuth2 authentication to your project a breeze. Follow the instructions above to integrate social logins into your app quickly and efficiently!

