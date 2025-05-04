from catalog.models import Product
from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

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

    def clean_price(self):
        price = int(self.cleaned_data["price"])
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price
