from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk) [0:3]# exclude the current item
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})  

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.pk)

    else:
        form = NewItemForm()
    form = NewItemForm()
    return render(request, 'item/form.html', {'form': form, 'title': 'New Item'})