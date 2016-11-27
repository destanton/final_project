from haystack import indexes
from sherlock.models import Profile, About
from haystack.utils import Highlighter



# class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.EdgeNgramField(document=True, use_template=True)
#     # suggestions = indexes.FacetCharField()
#     #
#     # def prepare(self, obj):
#     #     prepared_data = super(ProfileIndex, self).prepare(obj)
#     #     prepared_data["suggestions"] = prepared_data["text"]
#     #     return prepared_data
#
#     def get_model(self):
#         return Profile
#
#     def index_queryset(self, using=None):
#         return Profile.objects.all()


class AboutIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    eye_color = indexes.CharField(model_attr="eye_color", boost=2)
    # suggestions = indexes.FacetCharField()
    #
    # def prepare(self, obj):
    #     prepared_data = super(AboutIndex, self).prepare(obj)
    #     prepared_data["suggestions"] = prepared_data["text"]
    #     return prepared_data

    def get_model(self):
        return About

    def index_queryset(self, using=None):
        return About.objects.all()
