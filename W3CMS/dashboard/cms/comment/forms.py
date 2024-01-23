from django import forms
from dashboard.cms.comment.models import Comment
from mptt.forms import TreeNodeChoiceField



class BlogCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False
        self.fields['status'].widget.attrs.update(
            {'class': 'd-none'})

    class Meta:
        model = Comment
        fields = ('name', 'parent', 'email', 'content','status')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows' : '8','placeholder' : 'Add a Comment' }),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(BlogCommentForm, self).save(*args, **kwargs)
    
