# Django Ecommerce Headless API
# Introduction
 This repository contains code and notes to get a working django Ecommerce api application
 using Django rest framework and Django rest auth , JWT for authentication and
 Django all-auth for social authentication and Stripe api is used for payments
 handling of the app and Documentation for the project is done by using the
 swagger api package for Django.

# Packages 

- [Packages](#packages)
  - [Authentication](#authentication)
  - [Authorization](#authorization)
  - [Documentation](#documentation)

## Packages

  ### Authentication
  * [django-rest-passwordreset](https://github.com/anx-ckreuzberger/django-rest-passwordreset): Password reset endpoints that hook into Django Authentication system
  * [djoser](https://github.com/sunscrapers/djoser): REST implementation of Django authentication system
  * [django-rest-auth](https://github.com/Tivix/django-rest-auth/): A set of REST API endpoints to handle User Registration and Authentication tasks - ( **on pause and is currently unsupported**, [but there is a newer fork](https://github.com/jazzband/dj-rest-auth) )
  * [django-rest-registration](https://github.com/apragacz/django-rest-registration): User registration and authentication REST API, based on Django REST Framework.
  * [django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt/): JSON Web Token Authentication support for Django REST Framework - ( **currently unmaintained**, [but there is a newer fork](https://github.com/Styria-Digital/django-rest-framework-jwt) )
  * [django-rest-framework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt): A JSON Web Token authentication plugin for the Django REST Framework
  * [django-rest-framework-social-oauth2](https://github.com/PhilipGarnero/django-rest-framework-social-oauth2): python-social-auth and oauth2 support for django-rest-framework
  * [django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit): Django OAuth Toolkit can help you providing out of the box all the endpoints, data and logic needed to add OAuth2 capabilities to your Django projects. Django OAuth Toolkit makes extensive use of the excellent OAuthLib, so that everything is rfc-compliant.

  ### Authorization

  * [dry-rest-permissions](https://github.com/dbkaplan/dry-rest-permissions): Rules based permissions for the Django Rest Framework

  ### Documentation
  * [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger): Swagger Documentation Generator for Django REST Framework (this package is deprecated and no longer maintained. It throw error as staticfiles template tag was deprecated in Django 2.2 and is finally removed in Django 3.0. it's recommended to use drf-yasg )
  * [drf-yasg](https://github.com/axnsan12/drf-yasg): Alternative OpenAPI Generator for Django REST Framework with response schema support
