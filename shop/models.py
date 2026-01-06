from django.db import models


# دسته‌بندی محصولات
class Category(models.Model):
    name = models.CharField(max_length=100)  # project, monaghese
    title = models.CharField(max_length=100)  # عنوان فارسی مثل "پروژه"

    def __str__(self):
        return self.title


class MediaItem(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('photo', 'عکس'),
        ('video', 'فیلم'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='gallery/')
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.title or 'آیتم'} - {self.get_media_type_display()}"

# class Category(models.Model):
#     name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
#     slug = models.SlugField(unique=True, verbose_name="شناسه لاتین")
#
#     class Meta:
#         verbose_name = "دسته‌بندی"
#         verbose_name_plural = "دسته‌بندی‌ها"
#
#     def __str__(self):
#         return self.name
#
#
# # محصول
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="دسته‌بندی")
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر محصول")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت")
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی انبار")
    is_available = models.BooleanField(default=True, verbose_name="موجود است؟")
    description = models.TextField(blank=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name
