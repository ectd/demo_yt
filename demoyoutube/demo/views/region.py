from django.shortcuts import render
from demo.models.region import region
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import CreateView, UpdateView
from demo.forms.region import regionForm
from django.urls import reverse_lazy


def region_list(request):
    selected            = "region"
    region_list    = region.objects.all()


    # Pagination : 10 éléments par page
    paginator = Paginator(region_list.order_by('-name'), 10)
    try :
        page = request.GET.get("page")
        if not page:
            page = 1
        region_list = paginator.page(page)
    except EmptyPage:

        # Si on dépasse ta limite de pages, on prend La dernière
        region_list = paginator.page(paginator.num_pages( ))
    return render(request, "demo/region/region_list.html", locals())

class Createregion(CreateView):
    model           = region
    form_class      = regionForm
    template_name   = "demo/region/region_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_region", kwargs={"pk": self.object.id})

class Updateregion(UpdateView):
    model           = region
    form_class      = regionForm
    template_name   = "demo/region/region_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_region", kwargs={"pk": self.object.id})        