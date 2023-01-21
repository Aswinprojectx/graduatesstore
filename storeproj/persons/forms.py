# from django import forms
#
# from persons.models import Person, SP
#
#
# class PersonCreationForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['specialization'].queryset = SP.objects.none()
#
#         if 'course' in self.data:
#             try:
#                 country_id = int(self.data.get('course'))
#                 self.fields['specialization'].queryset = SP.objects.filter(country_id=country_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['specialization'].queryset = self.instance.course.city_set.order_by('name')