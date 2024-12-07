# 🌐 Linkedin OAuth2 🔑 Guide

```note
Hi! Soon, Here will be the docs 📝 for LinkedIn provider!
```
# LINKEDIN OAUTH2 INTEGRATION

<div align="left" style="position: relative;">
<p align="left">
	<em>Seamlessly Integrate LinkedIn Authentication in Your Django Application!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/Hoka03/oauth_2_linkedin?style=default&logo=opensourceinitiative&logoColor=white&color=0A66C2" alt="license">
	<img src="https://img.shields.io/github/last-commit/Hoka03/oauth_2_linkedin?style=default&logo=git&logoColor=white&color=0A66C2" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Hoka03/oauth_2_linkedin?style=default&color=0A66C2" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Hoka03/oauth_2_linkedin?style=default&color=0A66C2" alt="repo-language-count">
</p>
<p align="left">
	<!-- Add dependency badges if needed -->
</p>
<p align="left">
	<!-- Add additional badges if needed -->
</p>
</div>
<br clear="right">

## 🔗 Quick Links

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
---

## 📍 Overview

This project demonstrates how to integrate LinkedIn OAuth2 authentication into a Django application. Users can authenticate via LinkedIn, retrieve their profile details, and access organization information. It's ideal for applications requiring professional user data.

---

## 👾 Features

| **Feature**              | **Description**                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------|
| **OAuth2 Authorization**  | Allows users to sign in via LinkedIn securely.                                              |
| **Profile Retrieval**     | Fetch user profile information, including name and email.                                   |
| **Organization Access**   | Retrieve organizational details based on user access.                                       |
| **Secure Integration**    | Implements industry-standard practices for token handling and API interaction.              |

---

## 📁 Project Structure

### 📂 Project Index

```plaintext
.
├── linkedin_oauth/         # Django application source
│   ├── views.py            # Core LinkedIn OAuth logic
│   ├── settings.py         # Project configuration
│   └── __init__.py         # Package initializer
├── .env                    # Environment variables (excluded from version control)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### ☑️ Prerequisites
- Python: Version 3.8 or higher
- Django: Version 4.x or higher
- LinkedIn Developer Account: Register your application to obtain API credentials.

### ⚙️ Installation
1.Clone the repository:
```commandline
git clone https://github.com/Hoka03/oauth_2_linkedin.git
cd oauth_2_linkedin
```
2.Set up a virtual environment:
```commandline
python -m venv venv
source venv/bin/activate
```
3.Install dependencies:
```commandline
pip install -r requirements.txt
```
4.Set up environment variables:
- Create a .env file in the project root:
```commandline
your_client_id=your_linkedin_client_id
your_client_secret_key=your_linkedin_client_secret
your_redirect_uri=http://localhost:8000/callback
```
- Replace placeholders with your LinkedIn app credentials.

5.Run database migrations:
```commandline
python manage.py migrate
```
6.Start the development server:
```commandline
python manage.py runserver
```

## 🤖 Usage

1.Authenticate via LinkedIn:
- Navigate to http://localhost:8000 in your browser.
- Click the "Login with LinkedIn" button to initiate the OAuth flow.

2.Grant permissions:
- Log in to LinkedIn and grant permissions requested by the app.

3.Fetch data:
- After successful login, view your LinkedIn profile information, such as name and email.



