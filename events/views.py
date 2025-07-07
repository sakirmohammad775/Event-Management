
# Create your views here.
from django.shortcuts import render
from events.forms import EventForm
from events.models import Event, Category, Participant

def home(request):
    form = EventForm()
    events = Event.objects.all()
    categories = Category.objects.all()
    participants = Participant.objects.all()

    print("Events:", events)
    print("Categories:", categories)
    print("Participants:", participants)

    context = {
        'form': form,
        'events': events,
        'categories': categories,
        'participants': participants,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
def manager(request):
    return render(request, 'home.html')

def create_event(request):
    
    return render(request, 'event_form.html')

# events/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Event, Participant, Category
# from .forms import EventForm, ParticipantForm, CategoryForm

# # ---------- EVENTS ----------
# def event_list(request):
#     events = Event.objects.all()
#     return render(request, 'events/event_list.html', {'events': events})

# def event_create(request):
#     form = EventForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('event_list')
#     return render(request, 'events/event_form.html', {'form': form})

# def event_update(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     form = EventForm(request.POST or None, instance=event)
#     if form.is_valid():
#         form.save()
#         return redirect('event_list')
#     return render(request, 'events/event_form.html', {'form': form})

# def event_delete(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('event_list')
#     return render(request, 'events/event_confirm_delete.html', {'event': event})


# # ---------- PARTICIPANTS ----------
# def participant_list(request):
#     participants = Participant.objects.all()
#     return render(request, 'events/participant_list.html', {'participants': participants})

# def participant_create(request):
#     form = ParticipantForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('participant_list')
#     return render(request, 'events/participant_form.html', {'form': form})

# def participant_update(request, pk):
#     participant = get_object_or_404(Participant, pk=pk)
#     form = ParticipantForm(request.POST or None, instance=participant)
#     if form.is_valid():
#         form.save()
#         return redirect('participant_list')
#     return render(request, 'events/participant_form.html', {'form': form})

# def participant_delete(request, pk):
#     participant = get_object_or_404(Participant, pk=pk)
#     if request.method == 'POST':
#         participant.delete()
#         return redirect('participant_list')
#     return render(request, 'events/participant_confirm_delete.html', {'participant': participant})


# # ---------- CATEGORIES ----------
# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'events/category_list.html', {'categories': categories})

# def category_create(request):
#     form = CategoryForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('category_list')
#     return render(request, 'events/category_form.html', {'form': form})

# def category_update(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     form = CategoryForm(request.POST or None, instance=category)
#     if form.is_valid():
#         form.save()
#         return redirect('category_list')
#     return render(request, 'events/category_form.html', {'form': form})

# def category_delete(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         category.delete()
#         return redirect('category_list')
#     return render(request, 'events/category_confirm_delete.html', {'category': category})
