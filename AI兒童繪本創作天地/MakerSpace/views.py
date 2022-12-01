from django.shortcuts import render
from .MakerSpace import PromptModelForm
from .models import MakerSpace
import torch
from diffusers import DiffusionPipeline , EulerDiscreteScheduler
import os 

# from django.http.response import HttpResponse

# Create your views here.
def index(request):
    form = PromptModelForm()

    if request.method == "POST":
        form = PromptModelForm(request.POST)
        prompt = request.POST.get('prompt')
        print(prompt)
        generate(prompt)
        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }

    # print(request.POST['prompt'])

    return render(request, 'gallery/index.html', context)
 
def generate(prompt):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_id =  "CompVis/stable-diffusion-v1-4"
    auth_token = "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"
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = DiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, use_auth_token = auth_token,revision="fp16", torch_dtype=torch.float16).to(device)

    # with autocast(device):
    image = pipe(prompt,  height=768, width=768).images[0]
    image.save("./templates/test.png")