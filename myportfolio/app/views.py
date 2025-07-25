import json
import os
from django.conf import settings
from django.shortcuts import render

data = {
    "nome": "iBDEV",
    "nom": "Ibrahim SAWADOGO ",
    "adresse": "Rue 17.418, Pissy Ouagadougou Burkina Faso",
    "email": "ibdev0101@gmail.com",
    "linkedin": "linkedin.com/in/ibrahim-swd",
    "github": "github.com/ibrahimsaw",
    "permis": "Permis A1 B C",
    "datenais": "1999-09-30",
    "tel": "+226 74 53 46 94 / +226 63 69 69 61",
    "description": "Développeur Full-Stack",
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
    "team_members": [
        {"name": "SAWADOGO Ibrahim", "role": "Developpeur", "image": "img/team-1.jpg"},
        # {"name": "Bob", "role": "Developer", "image": "img/team-2.jpg"},
        # {"name": "Charlie", "role": "Project Manager", "image": "img/team-3.jpg"},
    ],
    "skills": [
        {"name": "HTML", "level": 95, "color": "bg-primary"},
        {"name": "CSS", "level": 85, "color": "bg-warning"},
        {"name": "PHP", "level": 90, "color": "bg-danger"},
        {"name": "JavaScript", "level": 90, "color": "bg-danger"},
        {"name": "Angular JS", "level": 95, "color": "bg-dark"},
        {"name": "WordPress", "level": 85, "color": "bg-info"},
    ],

    "education": [
        {'side': 'left', 'animation': 'slideInLeft',
         "title": "UI Design Course", "school": "Cambridge University", "years": "2010 - 2014"},
        {'side': 'right', 'animation': 'slideInRight',
         "title": "iOS Development", "school": "MIT", "years": "2014 - 2016"},
        {'side': 'left', 'animation': 'slideInLeft',
         "title": "Web Design", "school": "Harvard", "years": "2012 - 2015"},
        {'side': 'right', 'animation': 'slideInRight',
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
    "projects_data": {
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

from django.views import View
from django.shortcuts import render
from django.conf import settings
import os
import json
from datetime import date

def calculer_age(datenais):
    today = date.today()
    return today.year - datenais.year - ((today.month, today.day) < (datenais.month, datenais.day))

# -------------------------
# ✅ Classe de base commune
# -------------------------
class BaseCVView(View):

    def get_services(self):
        json_path = os.path.join(settings.BASE_DIR, "app/static/json/data.json")
        try:
            with open(json_path, encoding="utf-8") as fichier:
                return json.load(fichier)
        except FileNotFoundError:
            return []

    def get_context(self):
        return {
            "data": data,
            "services": self.get_services()
        }


class HomeView(BaseCVView):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name, self.get_context())

class MonCView(BaseCVView):
    template_name = "cv.html"

    def get(self, request):
        return render(request, self.template_name, self.get_context())
