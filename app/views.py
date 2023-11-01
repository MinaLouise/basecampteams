from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass
from typing import List


# Create your views here.


@dataclass
class Team:
    name: str
    description: str
    members: List[str]


teams={
        'community': {
           'name': 'Community',
           'description': "Gets together events away from our work.",
           'members': ['Jordan','Joby','Aj','Micah','Caleb']
        },
        'documentation': {
            'name': 'Documentation', 
            'description': "Document the activities that are done at BCCA.", 
            'members': ['Mina', 'Kaleigh', 'Jay', 'Joshua', 'Kayleah', 'Blair', 'Conner']
        },
        'management': {
            'name': 'Management', 
            'description': "They are in charge of making sure the building is clean.",
            'members': ['Nick', 'Jeremiah', 'Ab', 'Abigail', 'Mathew', 'Owen']
        },
        'procurement': {
            'name': 'Procurement', 
            'description': "Get our lunch to gether.", 
            'members': ['Big John', 'Adrian', 'Bryce', 'Wyatt', 'Blaine']
        }
    }


def team_list(request: HttpRequest) -> HttpResponse:
    
    return render(request, "index.html", {'teams': teams})


def team_detail(request: HttpRequest, team_name):
    # Lookup the appropriate team using a dictionary or database query
    team = teams.get(team_name)  # Replace with your actual data lookup
    context = {'team': team}
    return render(request, 'teams.html', context)