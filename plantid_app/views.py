from django.shortcuts import render
from .forms import PlantImageForm
from .models import PlantImage

# Create your views here.
def upload_image(request):
    
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PlantImageForm()
    images= PlantImage.objects.all().order_by('-uploaded_at')
    return render(request,'plantid_app/upload.html', {
        'form': form, 
        'images': images
        })
   