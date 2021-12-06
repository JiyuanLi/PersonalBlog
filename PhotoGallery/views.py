from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Image


# Create your views here.
class IndexView(generic.ListView):
    template_name = "PhotoGallery/index.html"
    context_object_name = "image_list"

    def get_queryset(self):
        return Image.objects.order_by('id')[:5]


class DetailView(generic.DetailView):
    model = Image
    template_name = "PhotoGallery/detail.html"
    context_object_name = "image"


def vote(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    try:
        selected_option = request.POST['choice']
    except Exception as e:
        context = {
            'image': image,
            'error_message': "No Choice was selected"
        }
        return render(request, "PhotoGallery/detail.html", context=context)
    else:
        if selected_option == "like":
            image.image_like += 1
        elif selected_option == "dislike":
            image.image_dislike += 1
        image.save()
        return HttpResponseRedirect(reverse('PhotoGallery:PhotoGalleryIndex'))

