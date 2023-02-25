
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('mualliflar/', mualliflar),
    path('kitoblar/', kitoblar),
    path('talabalar/', talabalar),
    path('qaydlar/', qaydlar),
    path('muallif/<int:son>/', bitta_muallif),  # talaba/5/
    path('kitob/<int:son>/', bitta_kitob),  # talaba/5/
    path('talaba/<int:son>/', bitta_talaba),  # talaba/5/
    path('qayd/<int:son>/', bitta_record),  # talaba/5/
    path('sahifa/', kitob_1),
    path('badiiy/', kitob_2),
    path('kitob_oz/', kitob_3),
    path('tirik_kitob/', kitob_4),
    path('kitob_0/', kitobi_0),
    path('talaba_ism/', talaba_ism),
    path('muallif_erkak/', muallif_erkak),
    path('muallif_ayol/', muallif_ayol),
    path('kitob_soni/', muallif_1),
    path('tirik/', muallif_2),
    path('olingan_sana/', record_1),
    path('bitiruvchi_qayd/', record_2),
    path('bitiruvchi/', bitiruvchi),
    path('muallif_qosh/', muallif_qosh),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('record_ochir/<int:son>/', muallif_ochir),

]
