from catalog.models import Product
from django.forms import ModelForm, BooleanField, ImageField
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class ProductForm(ModelForm):
    #  список запрещенных слов
    FORBIDDEN_WORDS = [
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
    image = ImageField(validators=[FileExtensionValidator(['jpg', 'png'],
                                                          'Поддерживается загрузка "png" и "jpg')])

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

    def clean_name(self):
        name = self.cleaned_data["name"]
        for word in self.FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError(
                    f"Такое имя не допустимо исключите следующие имена: {self.FORBIDDEN_WORDS}"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for word in self.FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError(
                    f"Такое описание не допустимо исключите следующие имена: "
                    f"{self.FORBIDDEN_WORDS}"
                )
        return description

    def clean_price(self):
        price = int(self.cleaned_data["price"])
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Максимальный размер файла 5 МВ ')
        return image
