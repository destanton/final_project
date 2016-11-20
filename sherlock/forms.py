from django import forms
from sherlock.models import About, Profile
from haystack.forms import HighlightedModelSearchForm

class AutoModelSearchForm(HighlightedModelSearchForm):
