from django.db import models

# Create your models here.


class Muallif(models.Model):
    JINS = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    ]
    ism = models.CharField(max_length=40)
    tugulgan_yil = models.DateField()
    tirik = models.BooleanField()
    kitob_soni = models.PositiveIntegerField()
    jins = models.CharField(max_length=10, choices=JINS)

    def __str__(self) -> str:
        return self.ism


class Kitob(models.Model):
    JANR = [
        ("Badiiy", "Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli")
    ]
    nom = models.CharField(max_length=70)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=12, choices=JANR)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom


class Talaba(models.Model):
    ism = models.CharField(max_length=40)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()
    bitiruvchi = models.BooleanField()

    def __str__(self) -> str:
        return self.ism


class Admin(models.Model):
    ISH_VAQTI = [
        ("8:00 - 12:00", "8:00 - 12:00"),
        ("13:00 - 17:00", "13:00 - 17:00"),
    ]
    ism = models.CharField(max_length=40)
    ish_vaqti = models.CharField(max_length=20, choices=ISH_VAQTI)

    def __str__(self) -> str:
        return self.ism + " " + self.ish_vaqti


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qay_sana = models.DateField(blank=True, null=True)

    # def __str__(self) -> str:
    #     return self.talaba.ism + "-" + self.kitob.nom
