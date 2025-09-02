from transformers import AutoModelForImageClassification
from PIL import Image
from torchvision import transforms
import torch
import pandas as pd

# 自定义图像预处理
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

df = pd.read_csv("data/metadata.csv", sep=";", usecols=["species_id", "species"])
df = df.drop_duplicates().sort_values("species_id").reset_index(drop=True)
label2info = {i: (row["species_id"], row["species"]) for i, row in df.iterrows()}

# 加载模型（只加载一次）
model = AutoModelForImageClassification.from_pretrained("gerald29/plantclef2024")
model.eval()


def predict_plant(image_path):
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        predicted_class_idx = output.logits.argmax(-1).item()

    species_id, latin_name = label2info.get(predicted_class_idx, ("Unknown", "Unknown"))
    return {
        "label": predicted_class_idx,
        "species_id": species_id,
        "latin_name": latin_name,
    }
