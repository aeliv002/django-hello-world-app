import textwrap

from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse

from django.views import generic
from .models import City

class HomePageView(generic.View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)

def healthCheck(request):
    return JsonResponse({'status':'ok'})

class MyCreateView(generic.CreateView):
    template_name = 'form_template.html'
    fields = '__all__'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super(MyCreateView, self).get_context_data(**kwargs)

        if "HTTP_REFERER" in self.request.META:
            context['emptyNav'] = self.request.META['HTTP_REFERER'] == self.request.build_absolute_uri(reverse('persons-table'))

        return context


class CreateCity (MyCreateView):
    model = City
