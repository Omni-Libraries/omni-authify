# Omni-Authify Documentation

Omni-Authify is a Python library that makes it easy to add OAuth2 authentication to your applications. This documentation will guide you through installation, usage, and configuration.

## 📚 Table of Contents
- [Usage Guides](#usage-guides)
- [Supported Providers](providers.md)
- [Contributing](../CONTRIBUTING.md)
- [License](../LICENSE)

---

## 🛠️ Installation Guide

### 🚀 Quick Start

Install Omni-Authify using pip:

```bash
pip install omni-authify
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
var = {
    'client_id': 'YOUR_APP_ID',
    'client_secret': 'YOUR_APP_SECRET',
    'redirect_uri': 'YOUR_REDIRECT_URI',
    'scope': 'email,public_profile'
}
```

#### Google

```python
var = {
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET',
    'redirect_uri': 'YOUR_REDIRECT_URI',
    'scope': 'email profile'
}
```

#### 🌟 [More Provider Configurations Coming Soon...]

---

## 📜 License

Omni-Authify is licensed under the MIT License. See the [LICENSE file](../LICENSE) for details.

---

Omni-Authify makes adding OAuth2 authentication to your project a breeze. Follow the instructions above to integrate social logins into your app quickly and efficiently!

