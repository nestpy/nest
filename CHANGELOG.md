# Changelog

## [0.2.0] - Initial Release (2024-12-22)

A Python backend framework inspired by NestJS [@https://github.dev/nestpy/nest/tree/develop/nest/core]

### Features

- Implemented a simple HTTP server with FastAPI
- Created dependency injection container
- Added module system for application organization
- Added controller and service decorators 
- Added http method decorators (GET, POST, PUT, DELETE, PATCH)
- Added API versioning (URI-based)
- Added GlobalPrefix support


### Project Organization
```
src/nest/
├── common/
│   ├── decorators/
│   ├── enums/
│   └── interfaces/
└── core/
    ├── application.py
    ├── container.py
    └── nest_factory.py
```

### Technical Implementation
- Full type hinting support
- FastAPI integration
- Uvicorn server implementation
- Automatic dependency resolution
- Path normalization
- Modular architecture

This initial release provides a solid foundation for building scalable Python web applications using familiar NestJS patterns while leveraging Python's type system and modern web capabilities.