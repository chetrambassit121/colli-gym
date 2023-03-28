from django import forms

from .models import Comment, MessageModel, Post


class ExploreForm(forms.Form):
    query = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Explore tags"})
    )


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": "7", "cols": "30", "placeholder": "Create a post...", "name":"msg", "class": "form-control"}),
    )
# name="msg" id=""msg cols="30" rows="5" class="form-control" style="background-color: black;"
    image = forms.ImageField(
        required=False, widget=forms.ClearableFileInput(attrs={"multiple": True})
    )

    video = forms.FileField(
        required=False, widget=forms.ClearableFileInput(attrs={"multiple": True})
    )

    class Meta:
        model = Post
        fields = ["body", "image", "video"]


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("body", "image")
        widgets = {
            "body": forms.TextInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": "3", "placeholder": ""}),
    )

    class Meta:
        model = Comment
        fields = ["comment"]


# class ReplyForm(forms.ModelForm):
#     comment = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={'rows': '3', 'placeholder': 'Leave a Reply...'})
#     )

#     class Meta:
#         model = Comment
#         fields = ['comment']


class ThreadForm(forms.Form):
    username = forms.CharField(label="", max_length=100)


class MessageForm(forms.ModelForm):
    body = forms.CharField(
        label="", max_length=1000, widget=forms.Textarea(attrs={"rows": "3",})
    )

    image = forms.ImageField(required=False)

    class Meta:
        model = MessageModel
        fields = ["body", "image"]


class ShareForm(forms.Form):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": "1", "placeholder": "Share..."}),
    )

    class Meta:
        model = MessageModel
        fields = ["body"]
