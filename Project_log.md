Project Log: PlantID Web Application

Overview

This project is a web-based plant identification system developed with Django and PyTorch. It allows users to upload plant images and receive species predictions using a pre-trained model from Hugging Face. The project integrates a machine learning pipeline into a user-facing interface for real-time inference.

Milestones

Environment Setup

✅ Created Python virtual environment using venv

✅ Installed required packages: Django, torch, transformers, pillow, pandas

✅ Fixed issues with Anaconda interfering with virtual environment

Django Project Setup

✅ Created Django project plantid_project and app plantid_app

✅ Configured settings, URLs, and media path

Image Upload Feature

✅ Created PlantImage model to store uploaded images

✅ Built upload form using ModelForm

✅ Designed upload page with HTML

✅ Displayed most recent image and result after upload

Model Integration

✅ Selected model: gerald29/plantclef2024 (DINOv2)

✅ Developed inference.py to handle preprocessing, prediction, and label mapping

✅ Loaded model with transformers.AutoModelForImageClassification

✅ Used custom label2species mapping from PlantCLEF metadata

Metadata Processing

✅ Downloaded PlantCLEF metadata CSV (~700MB)

✅ Parsed and extracted species_id and species name

✅ Built label2species and species2label dictionaries

UI Enhancement

✅ Displayed prediction result in the UI

✅ Switched from full list to "latest image only"

✅ Prepared for "history view" button (JS feature pending)

Version Control

✅ Initialized Git repository

✅ Committed in English: Implemented plant image upload and classification

✅ Pushed to GitHub repository

Next Steps



Notes

Metadata label IDs do not directly map to model output indices; custom mapping was built

The prediction output is a numerical label which needs to be converted via label2species

Project currently runs in a local development environment only

Author

Wen Liu, 2025