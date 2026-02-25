TechPulse – AI Tools & Global Tech News Intelligence Portal
Project Overview

TechPulse is a Django-based web application that allows users to explore trending Artificial Intelligence tools and view related global technology news on a centralized platform.

The system organizes AI tool information and associated news articles using structured database relationships. It dynamically retrieves and displays data through Django’s backend framework, providing a clean and user-friendly interface.

Core Features

Manage AI tools with name, company, category, description, and trending status

View detailed information about each AI tool

Display related news articles using ForeignKey relationships

Search tools by name

Filter tools by category and trending status

Add new AI tools using Django CreateView

Modular URL configuration using separate urls.py files

Template inheritance using base.html

Dynamic database-driven content rendering

Static file management for CSS styling

Project Structure

The project consists of two Django applications:

1. Tools App

Manages AI tool information:

Name

Company

Category

Description

Trending status

2. News App

Manages technology news articles:

Title

Content

Source URL

Published Date

Linked to AI tools using ForeignKey relationship

Django Concepts Implemented

Function-Based Views

Class-Based Generic Views (ListView, DetailView, CreateView)

Django Models and database relationships

HttpRequest handling using request.GET

HttpResponse rendering using render()

Filtering and search functionality

Django Template Language (variables, loops, conditions, filters)

Template inheritance

Static file configuration

MySQL database integration

Tech Stack

Python

Django

MySQL

HTML5


Future Improvements

News detail page

Pagination

Advanced filtering

User authentication

Deployment to cloud platform

This project is developed for academic and educational purposes.

CSS3

Git & GitHub
