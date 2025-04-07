import json
import os
from django.conf import settings
from django.shortcuts import render


def home(request):
    json_path = os.path.join(settings.BASE_DIR, "app/static/json/data.json")

    try:
        with open(json_path, encoding="utf-8") as fichier:
            services = json.load(fichier)
    except FileNotFoundError:
        data = {
            "nome":"iBDEV",
            "nom": "Ibrahim SAWADOGO ",
    "adresse": "zongo,Ouagadougou,Burkina Faso",
    "email":"ibdev0101@gmail.com",
    "tel":"+226 74 53 46 94 / +226 63 69 69 61",
    "description": "Développeur Flutter et Django",
    "competences": ["Flutter", "Django", "Python", "Google Maps API"],
    "projets": [
        {
            "titre": "Application de covoiturage",
            "annee": 2024,
            "technologies": ["Flutter", "Django", "PostgreSQL"]
        },
        {
            "titre": "Gestion des transports",
            "annee": 2025,
            "technologies": ["Django", "React"]
        }
    ],
    "team_members" :[
            {"name": "SAWADOGO Ibrahim", "role": "Developpeur", "image": "img/team-1.jpg"},
            #{"name": "Bob", "role": "Developer", "image": "img/team-2.jpg"},
            #{"name": "Charlie", "role": "Project Manager", "image": "img/team-3.jpg"},
        ],
            "skills" : [
            {"name": "HTML", "level": 95, "color": "bg-primary"},
            {"name": "CSS", "level": 85, "color": "bg-warning"},
            {"name": "PHP", "level": 90, "color": "bg-danger"},
            {"name": "JavaScript", "level": 90, "color": "bg-danger"},
            {"name": "Angular JS", "level": 95, "color": "bg-dark"},
            {"name": "WordPress", "level": 85, "color": "bg-info"},
        ],


        "education":[
            {'side': 'left','animation': 'slideInLeft',
             "title": "UI Design Course", "school": "Cambridge University", "years": "2010 - 2014"},
            {'side': 'right','animation': 'slideInRight',
             "title": "iOS Development", "school": "MIT", "years": "2014 - 2016"},
            {'side': 'left','animation': 'slideInLeft',
             "title": "Web Design", "school": "Harvard", "years": "2012 - 2015"},
            {'side': 'right','animation': 'slideInRight',
             "title": "Apps Design", "school": "Stanford", "years": "2016 - 2019"},
        ],
            "experiences": [
            {
                'side': 'left',
                'animation': 'slideInLeft',
                'date': '2045 - 2050',
                'title': 'Web Developer',
                'company': 'Soft Agency, San Francisco, CA',
                'description': 'Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.'
            },
            {
                'side': 'right',
                'animation': 'slideInRight',
                'date': '2045 - 2050',
                'title': 'Web Developer',
                'company': 'Soft Agency, San Francisco, CA',
                'description': 'Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.'
            },
            {
                'side': 'left',
                'animation': 'slideInLeft',
                'date': '2045 - 2050',
                'title': 'Web Developer',
                'company': 'Soft Agency, San Francisco, CA',
                'description': 'Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.'
            },
            {
                'side': 'right',
                'animation': 'slideInRight',
                'date': '2045 - 2050',
                'title': 'Web Developer',
                'company': 'Soft Agency, San Francisco, CA',
                'description': 'Lorem ipsum dolor sit amet elit. Aliquam odio dolor, id luctus erat sagittis non. Ut blandit semper pretium.'
            }
        ],
            "projects_data" : {
            "section_title": "My Projects",
            "filters": [
                {"name": "All Projects", "filter": "*", "active": True},
                {"name": "UI/UX Design", "filter": ".first", "active": False},
                {"name": "Graphic Design", "filter": ".second", "active": False}
            ],
            "projects": [
                {
                    "category": "first",
                    "image": "img/project-1.jpg",
                    "view_link": "img/project-1.jpg",
                    "detail_link": "#"
                },
                {
                    "category": "second",
                    "image": "img/project-2.jpg",
                    "view_link": "img/project-2.jpg",
                    "detail_link": "#"
                },
                {
                    "category": "first",
                    "image": "img/project-3.jpg",
                    "view_link": "img/project-3.jpg",
                    "detail_link": "#"
                },
                {
                    "category": "second",
                    "image": "img/project-4.jpg",
                    "view_link": "img/project-4.jpg",
                    "detail_link": "#"
                },
                {
                    "category": "first",
                    "image": "img/project-5.jpg",
                    "view_link": "img/project-5.jpg",
                    "detail_link": "#"
                },
                {
                    "category": "second",
                    "image": "img/project-6.jpg",
                    "view_link": "img/project-6.jpg",
                    "detail_link": "#"
                }
            ]
        },
        }
  # Si le fichier n'existe pas, retourner une liste vide

    return render(request, "home.html", {"data": data})
