###### <h1 align="center">Simplify OAuth2 Authentication</h1>

---
<p align="center">
    <a href="https://mukhsin-gitbook.gitbook.io/omni-authify/">
        <img src="https://img.shields.io/static/v1?message=Documented%20on%20GitBook&logo=gitbook&logoColor=ffffff&label=%20&labelColor=5c5c5c&color=3F89A1" alt="Documentation"/>
    </a>
    <a href="https://github.com/Omni-Libraries/omni-authify.git">
        <img src="https://img.shields.io/badge/Open_Source-❤️-FDA599?"/>
    </a>
    <a href="https://discord.gg/BQrvDpcw">
        <img src="https://img.shields.io/badge/Community-Join%20Us-blueviolet" alt="Community"/>
    </a>
    <a href="https://github.com/Omni-Libraries/omni-authify/issues">
        <img src="https://img.shields.io/github/issues/Omni-Libraries/omni-authify" alt="Issues"/>
    </a>
</p>

---


Omni-Authify is a Python library that makes OAuth2 authentication a breeze across multiple frameworks and providers. Its main goal is to give you a unified and easy-to-use interface for adding social logins to your applications.

## ✨ Features

- **🌍 Multiple Providers**: Currently supports Facebook OAuth2 authentication, with more to come.
- **🔧 Framework Integration**: Works seamlessly with Django, Django REST Framework (DRF), FastAPI and Flask.
- **⚡ Easy to Use**: Requires minimal setup to get started.
- **🚀 Extensible**: Designed to support more providers and frameworks as your needs grow.

## 📚 Table of Contents

- [Installation](installation.md)
- [Supported Providers and Frameworks](providers.md)
- [License](usage/LICENSE.md)

---

## 🚀 Usage Examples

Follow the example below to quickly integrate Omni-Authify into your application.

```python
from omni_authify.providers import Facebook

# Initialize the provider
facebook_provider = Facebook(
    client_id='your-client-id',
    client_secret='your-client-secret',
    redirect_uri='your-redirect-uri'
)

# Get authorization URL
auth_url = facebook_provider.get_authorization_url(state='your-state')

# After redirect and code exchange
access_token = facebook_provider.get_access_token(code='authorization-code')

# Fetch user profile
user_info = facebook_provider.get_user_profile(access_token, fields='your-fields')
```

---

## 🛠️ Installation Guide

Check out the full installation guide [here](installation.md) for detailed instructions on how to add Omni-Authify to your project.

## 📜 Supported Providers and Frameworks

Omni-Authify currently supports Facebook OAuth2 and integrates smoothly with Django, Django REST Framework (DRF), 
FastAPI and Flask. For a list of all supported providers and more details, check [this page](providers.md).

## 🔐 License

This project is licensed under the MIT License. See the [LICENSE file](../LICENSE) for more information.

---

Omni-Authify is your go-to solution for easy social login integration, whether you're building a simple python 
project or scaling up with DRF or other frameworks like FastAPI or Flask. Give it a spin and enjoy smooth OAuth2 
authentication!

