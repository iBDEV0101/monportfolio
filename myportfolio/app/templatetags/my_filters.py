from datetime import date, datetime
from django import template

register = template.Library()


@register.filter
def age(birthdate):
    if isinstance(birthdate, str):
        try:
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
        except ValueError:
            return "Date invalide"

    today = date.today()
    return today.year - birthdate.year - (
            (today.month, today.day) < (birthdate.month, birthdate.day)
    )
