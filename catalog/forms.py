from catalog.models import Product
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
#  список запрещенных слов
    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):
        name = self.cleaned_data["name"]
        for word in self.forbidden_words:
            if word in name.lower():
                raise ValidationError(
                    f"Такое имя не допустимо исключите следующие имена: {self.forbidden_words}"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for word in self.forbidden_words:
            if word in description.lower():
                raise ValidationError(
                    f"Такое описание не допустимо исключите следующие имена: "
                    f"{self.forbidden_words}"
                )
        return description
