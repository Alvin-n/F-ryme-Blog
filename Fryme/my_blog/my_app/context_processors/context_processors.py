from my_app.models import NavbarModel

def h_and_f(request):
    context = {}
    
    navbar_queryset = NavbarModel.objects.all()

    context['navbar_queryset'] = navbar_queryset
    
    return context