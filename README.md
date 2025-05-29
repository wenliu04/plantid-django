🌿 PlantID - Plant Species Identifier Web App

PlantID is a Django-based web application that allows users to upload photos of plants and automatically predicts the species using a pre-trained computer vision model. The project leverages a DINOv2-based image classification model trained on the PlantCLEF2024 dataset.

🚀 Features

📤 Upload plant images via a simple web interface

🧠 Predict plant species using a Hugging Face-hosted model

🔁 Display the prediction result (species ID and Latin name)

🖼️ View the latest uploaded image and prediction

📚 Maintain upload history (toggle feature in progress)

🛠️ Tech Stack

Backend: Python, Django

Frontend: HTML (with basic CSS), Django Templates

ML Model: gerald29/plantclef2024 (based on facebook/dinov2-base)

Data: PlantCLEF2024 metadata with species_id ↔ label mapping via CSV

📂 Project Structure

plantid_project/
├── plantid_app/
│   ├── templates/plantid_app/upload.html  # Upload form and display
│   ├── models.py                         # Image model with predicted label
│   ├── forms.py                          # Upload form
│   ├── views.py                          # Main view logic
│   ├── inference.py                      # Prediction logic using HF model
│   └── urls.py                           # App-level routing
├── plantid_project/
│   └── settings.py / urls.py             # Django config
├── data/                                 # PlantCLEF2024 metadata
│   └── PlantCLEF2024_metadata.csv
├── manage.py
└── README.md                             # You're reading it!

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/yourusername/plantid.git
cd plantid

2. Create & Activate a Virtual Environment

python -m venv plantid.venv
source plantid.venv/bin/activate   # On Windows: plantid.venv\Scripts\activate

3. Install Required Packages

pip install -r requirements.txt

Or manually:

pip install django transformers torch torchvision pandas pillow

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Run the Development Server

python manage.py runserver

Then open your browser and go to http://127.0.0.1:8000/

📊 Metadata & Label Mapping

We use PlantCLEF2024_metadata.csv to extract a mapping between model output labels and species IDs with Latin names. This mapping is used to present human-readable results in the UI.

📝 Todo



🧠 Model Info

Source: gerald29/plantclef2024

Architecture: ViT base patch 14 (DINOv2)

Classes: ~7,800 species

Trained on: Pl@ntNet + GBIF-sourced images

Label Output: 0 ~ N numeric class index → mapped via metadata

📄 License

MIT License. See LICENSE file for details.

🙋‍♀️ Author

Created by Wen Liu.If you find this helpful, feel free to ⭐️ this repo and contribute!