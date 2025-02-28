from django import forms
from tempus_dominus.widgets import DateTimePicker
from Box.models import Player, STATUS, POSITION, OBSERV, POINTS, \
    ObservationForm, ObservationList, Comments


class PlayerForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię', widget=forms.TextInput
        (attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nazwisko', widget=forms.TextInput
        (attrs={'class': 'form-control'}))
    year_of_birth = forms.IntegerField(min_value=1900, max_value=2050, label='Rocznik',
         widget=forms.NumberInput(attrs={'class': 'form-control'}))
    club = forms.CharField(label='Klub', widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.ChoiceField(choices=POSITION, label='Pozycja',
         widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS, label='Status', widget=forms.Select(attrs={'class': 'form-control'}))
    mail = forms.EmailField\
        (required=False, label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField\
        (required=False, label='Numer telefonu', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    agent = forms.CharField(required=False, label='Kontakt do agenta',
                            widget=forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = Player
        fields = '__all__'

class ObservationFormForm(forms.ModelForm):

    # scout = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label='Scout',
    #      widget=forms.Select(attrs={'class': 'form-control'}))
    player = forms.ModelChoiceField(queryset=Player.objects.all(), label='Piłkarz',
         widget=forms.Select(attrs={'class': 'form-control'}))
    observation = forms.ChoiceField(choices=OBSERV, label='Rodzaj obserwacji', widget=forms.Select(attrs={'class': 'form-control'}))
    first_desc = forms.CharField(label='Gra w ofensywie',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    second_desc = forms.CharField(label='Gra w defensywie',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    third_desc = forms.CharField(label='Gra bez piłki',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    fourth_desc = forms.CharField(label='Cechy wolicjonalne',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    fifth_desc = forms.CharField(label='Inne',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    sixth_desc = forms.CharField(label='Wnioski',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    one = forms.ChoiceField(choices=POINTS, label='Technika użytkowa',
         widget=forms.Select(attrs={'class': 'form-control'}))
    two = forms.ChoiceField(choices=POINTS, label='Gra słabszą nogą',
         widget=forms.Select(attrs={'class': 'form-control'}))
    three = forms.ChoiceField(choices=POINTS, label='Siła',
         widget=forms.Select(attrs={'class': 'form-control'}))
    four = forms.ChoiceField(choices=POINTS, label='Koordynacja',
         widget=forms.Select(attrs={'class': 'form-control'}))
    five = forms.ChoiceField(choices=POINTS, label='Przyspieszenie',
         widget=forms.Select(attrs={'class': 'form-control'}))
    six = forms.ChoiceField(choices=POINTS, label='Agresja',
         widget=forms.Select(attrs={'class': 'form-control'}))
    seven = forms.ChoiceField(choices=POINTS, label='Odpowiedzialność w grze',
         widget=forms.Select(attrs={'class': 'form-control'}))
    eight = forms.ChoiceField(choices=POINTS, label='Skłonność do przecinania linii przeciwnika(wejściem/podaniem)',
         widget=forms.Select(attrs={'class': 'form-control'}))
    nine = forms.ChoiceField(choices=POINTS, label='Pracowitość',
         widget=forms.Select(attrs={'class': 'form-control'}))
    ten = forms.ChoiceField(choices=POINTS, label='Odbiór piłki',
         widget=forms.Select(attrs={'class': 'form-control'}))
    eleven = forms.ChoiceField(choices=POINTS, label='Gra w powietrzu',
         widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = ObservationForm
        exclude = ['scout']



class Calendar(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'], label= 'Data i godzina', widget=forms.widgets.DateTimeInput(attrs={'id': 'datetimepicker', 'type': 'datetime'}))
    match = forms.CharField(label='Mecz', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Miasto', widget=forms.TextInput
        (attrs={'class': 'form-control'}))
    country = forms.CharField(label='Kraj', initial='Polska', widget=forms.TextInput
        (attrs={'class': 'form-control'}))
    # scout = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label='Scout',
    #      widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = ObservationList
        exclude = ['scout']


class CommentsForm(forms.ModelForm):
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = Comments
        exclude = ['player', 'date']
