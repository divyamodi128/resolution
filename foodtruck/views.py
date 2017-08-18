from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, BaseFormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse_lazy

from .models import Truck
from .forms import TruckForm

# Create your views here.
class ListTruckView(ListView):
    '''
    Get the List of all the Truck
    '''
    model = Truck
    context_object_name = 'truck_list'
    template_name = 'truck_lists.html'
    # form = TruckForm

    def get_context_data(self, **kwargs):
        context = super(ListTruckView, self).get_context_data(**kwargs)
        return context


class BaseTruckForm(BaseFormView):
    model = Truck
    form_class = TruckForm

    def get_initial(self):
        if not self.request.user.is_authenticated:
            return None
        return {'user': self.request.user}

    def get_context_data(self, **kwargs):
        context = super(BaseTruckForm, self).get_context_data(**kwargs)
        # import pdb ; pdb.set_trace()
        return context

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        print("Valid Forms")
        return super(BaseTruckForm, self).form_valid(form)
        # return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print("Invalid Form")
        if not self.request.user.id:
            form.errors['user'] = ['Not Autheticated, You need to Login First!']
        # import pdb ; pdb.set_trace()
        return self.render_to_response(self.get_context_data(form=form))


class CreateTruckView(BaseTruckForm, CreateView):
    '''
    User can register their truck with a short descriptions
    '''
    # model = Truck
    # form_class = TruckForm
    template_name = 'truck_create.html'
    success_url = '/truck/list/'
    # initial= {'user': self.request.user.id}

    def get_template_names(self):
        # import pdb ; pdb.set_trace()
        # if self.form_class.errors:
        #     if not self.request.user.is_authenticated:
        #         return 'message.html'
        return super(CreateTruckView, self).get_template_names()

class UpdateTruckView(BaseTruckForm, UpdateView):
    # model = Truck
    # queryset = Truck.objects.all()
    # fields = ['name']
    template_name = 'truck_update.html'
    success_url = '/truck/list/'

    def get_object(self, queryset=None):
        obj = super(UpdateTruckView, self).get_object(queryset)
        if obj.user == self.request.user:
            pass
        else:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                      {'verbose_name': queryset.model._meta.verbose_name})
        # import pdb ; pdb.set_trace()
        return obj


class DeleteTruckView(BaseTruckForm, DeleteView):
    # model = Truck
    template_name='truck_delete.html'
    success_url = reverse_lazy('truck-list')

# Not Used yet
class FormTruckView(FormView):
    template_name = 'truck_create.html'
    form_class = TruckForm
    success_url = '/truck/list/'

    def get_initial(self):
        # import pdb ; pdb.set_trace()
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden()
        return {'user': self.request.user.id}


class DetailTruckView(DetailView):
    model = Truck
    form_class = TruckForm
    template_name = 'truck_details.html'
    context_object_name = 'truckObj'
    # # def get_success_url(self):
    # #     return reverse('truck-detials', kwargs={'pk': self.object.pk})
    # # initial= {'user': self.request.user.id}
    def get_context_data(self, **kwargs):
        # import pdb ; pdb.set_trace()
        context = super(DetailTruckView, self).get_context_data(**kwargs)
        return context
    # def get_initial(self):
    #     import pdb ; pdb.set_trace()
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseForbidden()
    #     return {'user': self.request.user.id}


# class TruckformView(View):
#     form_class = TruckForm
#     # initial: {'user': request.user}

#     def get(self, request, *args, **kwargs):
#         form = self.form_class
#         return form

#     def post(self, request, *args, **kwargs):
#         return form


# class TruckFormView(FormView):
#     template_name = 'contact.html'
#     form_class = TruckForm
#     success_url = '/thanks/'

#     def form_valid(self, form, pk=None):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         if pk:
#             instance
#         return super(ContactView, self).form_valid(form)


def getLists(TruckListView):
    obj = Truck.objects.all()
    # import pdb ; pdb.set_trace()
    columns = ['SrNo', 'name', 'website', 'user', 'contact_no', 'emails']
    forms = TruckForm()
    # objSeralizer = FoodTruckSerializers(obj)
    return render(
        request,
        'truck_lists.html',
        {
            'columns': columns,
            'list': obj,
            'form': forms
        }
    )

@login_required(login_url='/accounts/login/')
def create(request):
    if request.method == 'POST':
        # import pdb ; pdb.set_trace()
        form = TruckForm(request.POST)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.user = request.user
            truck.save()
        return redirect('/truck/trucklist/')
    else:
        return Http404("Sorry Bad Request.")

@login_required()
def update(request, pk):
    if request.method == 'POST':
        truck = Truck.objects.get(id=pk)
        if request.user == truck.user:
            form = TruckForm(request.POST)
            if form.is_valid():
                truck = form.save(commit=False)
    return None
