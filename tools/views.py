from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .models import Tool


def tool_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    trending = request.GET.get('trending')

    tools = Tool.objects.all()

    if query:
        tools = tools.filter(name__icontains=query)

    if category:
        tools = tools.filter(category__icontains=category)

    if trending:
        tools = tools.filter(trending=True)

    return render(request, 'tools/tool_list.html', {
        'tools': tools,
        'query': query,
    })


class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'
    context_object_name = 'tool'


class ToolCreateView(CreateView):
    model = Tool
    fields = ['name', 'company', 'category', 'description', 'trending']
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tool_list')