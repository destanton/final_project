# from django import forms
# from sherlock.models import About, Profile
# from haystack.forms import HighlightedModelSearchForm
# from haystack.query import SearchQuerySet
#
#
# class AutoModelSearchForm(HighlightedModelSearchForm):
#     def search(self):
#         sqs = super(AutoModelSearchForm, self).search()
#         sqs = sqs.filter(biography_auto=self.cleaned_data['q'])
#
#         return sqs
