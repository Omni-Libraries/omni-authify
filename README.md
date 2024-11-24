# omni-authify
A Python package that supports OAuth2 authentication across multiple frameworks like Django, Django-DRF, Flask, and FastAPI.


omni-authify/
├── omni_authify/          # Main package directory
│   ├── __init__.py        # Package initializer
│   ├── core/              # Core functionality (common code shared across frameworks)
│   │   ├── __init__.py
│   │   ├── oauth.py       # Base OAuth2 implementation
│   │   ├── utils.py       # Utility functions (e.g., token parsing, URL generation)
│   │   ├── exceptions.py  # Custom exceptions for the library
│   ├── frameworks/        # Framework-specific integrations
│   │   ├── __init__.py
│   │   ├── django.py      # Django-specific logic
│   │   ├── drf.py         # Django REST Framework-specific logic
│   │   ├── flask.py       # Flask-specific logic
│   │   ├── fastapi.py     # FastAPI-specific logic
│   ├── providers/         # OAuth2 providers (Google, Facebook, etc.)
│   │   ├── __init__.py
│   │   ├── base.py        # Base class for all providers
│   │   ├── google.py      # Google provider implementation
│   │   ├── facebook.py    # Facebook provider implementation
│   │   ├── github.py      # GitHub provider implementation
│   │   ├── linkedin.py    # LinkedIn provider implementation
│   │   ├── twitter.py     # Twitter provider implementation
│   │   ├── telegram.py    # Telegram provider implementation
│   ├── settings.py        # Default configuration/settings for the library
│   ├── version.py         # Versioning info
├── tests/                 # Unit and integration tests
│   ├── __init__.py
│   ├── test_core.py       # Tests for core functionality
│   ├── test_frameworks/   # Tests for framework-specific integrations
│   │   ├── test_django.py
│   │   ├── test_flask.py
│   │   ├── test_fastapi.py
│   ├── test_providers/    # Tests for OAuth2 providers
│       ├── test_google.py
│       ├── test_facebook.py
│       ├── test_github.py
│       ├── test_twitter.py
├── docs/                  # Documentation for the library
│   ├── index.md           # Main README for documentation
│   ├── installation.md    # Installation guide
│   ├── usage/             # Usage guides for different frameworks
│   │   ├── django.md
│   │   ├── flask.md
│   │   ├── fastapi.md
│   ├── providers.md       # List of supported providers and usage examples
├── examples/              # Example projects demonstrating usage
│   ├── django_example/    # Django integration example
│   ├── flask_example/     # Flask integration example
│   ├── fastapi_example/   # FastAPI integration example
├── LICENSE -               # License file
├── README.md  -            # Main README for the project
├── setup.py               # Script for packaging and installation
├── requirements.txt       # Python dependencies
├── MANIFEST.in            # Additional files to include in the package
├── pyproject.toml         # Modern Python packaging configuration
└── .gitignore     -        # Files to ignore in Git
