from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from foodtruck.models import Truck
from .forms import MenuForm

class MenuCreate(View):
    form_class = MenuForm
    template_name = 'TruckMenu/list.html'

    def get(self, request, *args, **kwargs):
        if not request.user:
            print("Please login")
            return HttpResponseRedirect('/login/')
        # import pdb; pdb.set_trace()
        truck = Truck.objects.filter(user=request.user)[0]
        form = self.form_class(initial={'user': request.user, 'truck': truck})
        return render(request, self.template_name, {'menuFrom': form})

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'menuFrom': form})
