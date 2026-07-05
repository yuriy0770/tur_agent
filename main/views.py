from django.views.generic import ListView, DetailView, TemplateView
from .models import Category
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Country
from .forms import ReviewForm

class SearchView(ListView):
    model = Country
    template_name = 'main/search_results.html'
    context_object_name = 'results'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Country.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(hotel__icontains=query) |
                Q(cat__name_cat__icontains=query)
            ).distinct()
        return Country.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context



class AboutView(TemplateView):
    template_name = 'main/about.html'



class IndexView(ListView):
    """Главная страница с категориями и последними турами"""
    model = Country
    template_name = 'main/index.html'
    context_object_name = 'tours'

    def get_queryset(self):
        return Country.objects.all().order_by('-created')[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class CategoryDetailView(DetailView):
    """Детальная страница категории (список туров в категории)"""
    model = Category
    template_name = 'main/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        return Category.objects.get(slug_cat=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = self.object.countries.all()
        return context


class CountryDetailView(DetailView):
    model = Country
    template_name = 'main/country_detail.html'
    context_object_name = 'tour'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['form'] = ReviewForm()
        return context

@login_required
def add_review(request, slug):
    tour = get_object_or_404(Country, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.user = request.user
            review.save()
            messages.success(request, 'Спасибо за отзыв!')
    return redirect('main:country_detail', slug=slug)