from django.shortcuts import render
from demo.models.app_type import app_type
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import CreateView, UpdateView
from demo.forms.app_type import app_typeForm
from django.urls import reverse_lazy


def app_type_list(request):
    selected            = "app_type"
    app_type_list    = app_type.objects.all()


    # Pagination : 10 éléments par page
    paginator = Paginator(app_type_list.order_by('-name'), 10)
    try :
        page = request.GET.get("page")
        if not page:
            page = 1
        app_type_list = paginator.page(page)
    except EmptyPage:

        # Si on dépasse ta limite de pages, on prend La dernière
        app_type_list = paginator.page(paginator.num_pages( ))
    return render(request, "demo/app_type/app_type_list.html", locals())

class Createapp_type(CreateView):
    model           = app_type
    form_class      = app_typeForm
    template_name   = "demo/app_type/app_type_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_app_type", kwargs={"pk": self.object.id})

class Updateapp_type(UpdateView):
    model           = app_type
    form_class      = app_typeForm
    template_name   = "demo/app_type/app_type_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_app_type", kwargs={"pk": self.object.id})        