from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeLogo, HamaImage, KoshikImgae, ZenqerImage, AqsImage

class HomeListView(ListView):
    template_name = 'index.html'
    def get(self, request):
        logo = HomeLogo.objects.all()
        imagehama = HamaImage.objects.all()[0]
        koshikimage = KoshikImgae.objects.all()[0]
        zenqerimage = ZenqerImage.objects.all()[0]
        aqsimage = AqsImage.objects.all()[0]

        return render(request, self.template_name, context={'logo':logo,
                                                            'imagehama':imagehama,
                                                            'koshikimage':koshikimage,
                                                            'zenqerimage':zenqerimage,
                                                            'aqsimage':aqsimage})
# Create your views here.
