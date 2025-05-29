from django.shortcuts import render, redirect
from .forms import PlantImageForm
from .models import PlantImage
from .inference import predict_plant
from django.contrib import messages


def upload_image(request):
    prediction = None  # 初始化以避免 GET 请求报错
    latest_image = None  # 初始化以避免 GET 请求报错

    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save()  # 保存后得到对象
            image_path = plant_image.image.path
            result = predict_plant(image_path)
            prediction= result['latin_name']
            plant_image.predicted_label = result['label']
            plant_image.save()
            
            
    else:
        form = PlantImageForm()
    
    if PlantImage.objects.exists():
        latest_image = PlantImage.objects.latest('uploaded_at')

    
    return render(request, 'plantid_app/upload.html', {
        'form': form,
        'prediction': prediction,
        'image': latest_image
    })
