from django.shortcuts import render, redirect, get_object_or_404

from ..models import Venue, Artist, Note, Show
from ..forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator


def venue_list(request):
    form = VenueSearchForm()
    search_name = request.GET.get('search_name')

    if search_name:
        #search for this venue, display results
        venues = Venue.objects.filter(name__icontains=search_name).order_by('name')
    else :
        venues = Venue.objects.all().order_by('name')
        
    paginator = Paginator(venues, 25)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'lmn/venues/venue_list.html', { 'venues': page_object, 'form': form, 'search_term': search_name })


def artists_at_venue(request, venue_pk):   # pk = venue_pk
    """ Get all of the artists who have played a show at the venue with pk provided """

    shows = Show.objects.filter(venue=venue_pk).order_by('-show_date') 
    venue = Venue.objects.get(pk=venue_pk)
    
    paginator = Paginator(shows, 25)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'lmn/artists/artist_list_for_venue.html', { 'venue': venue, 'shows': page_object })


def venue_detail(request, venue_pk):
    venue = get_object_or_404(Venue, pk=venue_pk)
    return render(request, 'lmn/venues/venue_detail.html' , { 'venue': venue })
