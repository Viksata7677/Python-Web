from django import forms

from forumBasics.posts.models import Post


# class PersonForm(forms.Form):
#     STATUS_CHOICE = (
#         (1, 'Draft'),
#         (2, 'Published'),
#         (3, 'Archived')
#     )
#
#     person_name = forms.CharField(label = "Add your name",
#                                   widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
#                                   error_messages={'required': 'Please enter a value'}, required=True, max_length=10)
#     age = forms.IntegerField()
#     checkboxes = forms.MultipleChoiceField(label="Check", widget=forms.CheckboxSelectMultiple, choices=STATUS_CHOICE)
#     status = forms.IntegerField(widget=forms.Select(choices=STATUS_CHOICE))
#     is_lecturer = forms.BooleanField()
#     # status = forms.ChoiceField(choices=STATUS_CHOICE)

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ('title', 'content') Specific fields
        # exclude = ['title'] Everything without title.

        widgets = {
            'title': forms.NumberInput()
        }
        help_texts = {
            'title': "This is the title"
        }
        labels = {
            'title': "This is the title"
        }
        error_messages = {
            'title': {'required': "..."}
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search for a post...'})
    )
