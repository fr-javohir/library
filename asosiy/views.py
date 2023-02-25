from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request, 'home.html')


def mualliflar(request):
    qidiruv_soz = request.POST.get("qidirish")
    if qidiruv_soz is None:
        mf = Muallif.objects.all()
    else:
        mf = Muallif.objects.filter(ism__contains=qidiruv_soz)
    data = {
        "mualliflar": mf}
    return render(request, 'mualliflar.html', data)


def qaydlar(request):
    qidiruv_soz = request.POST.get("qidirish")
    if qidiruv_soz is None:
        rc = Record.objects.all()
    else:
        rc = Record.objects.filter(talaba__ism__contains=qidiruv_soz)
    data = {
        "qaydlar": rc
    }
    return render(request, 'record.html', data)


def talabalar(request):
    qidiruv_soz = request.GET.get("qidirish")
    if qidiruv_soz is None:
        talabalar = Talaba.objects.all()
    else:
        talabalar = Talaba.objects.filter(ism__contains=qidiruv_soz)
    data = {
        "talabalar": talabalar
    }
    return render(request, "talabalar.html", data)


def bitiruvchi(request):
    data = {
        "talabalar": Talaba.objects.filter(bitiruvchi=True)
    }
    return render(request, "bitiruvchi.html", data)


def kitobi_0(request):
    data = {
        "talabalar": Talaba.objects.filter(kitob_soni__gt=0),
        "xabar": "Kitobi 0 dan ko'p talabalar "
    }
    return render(request, "bitiruvchi.html", data)


def talaba_ism(request):
    data = {
        "talabalar": Talaba.objects.filter(ism__contains='a'),
        "xabar": "Ismida 'a' harfi qatnashgan talabalar "
    }
    return render(request, "bitiruvchi.html", data)


def muallif_erkak(request):
    data = {
        "mualliflar": Muallif.objects.filter(jins='Erkak'),
        "xabar": "Erkak mualliflar"
    }
    return render(request, "mualliflar.html", data)


def muallif_ayol(request):
    data = {
        "mualliflar": Muallif.objects.filter(jins='Ayol'),
        "xabar": "Ayol mualliflar"
    }
    return render(request, "mualliflar.html", data)


def muallif_qosh(request):
    if request.method == "POST":
        ism = request.POST.get("ism")
        t_yil = request.POST.get("t_yil")
        tirik = request.POST.get("tirik")
        k_soni = request.POST.get("k_soni")
        jins = request.POST.get("jins")

        Muallif.objects.create(ism=ism, tugulgan_yil=t_yil, tirik=True if tirik ==
                               'on' else False, kitob_soni=k_soni, jins=jins)
        data = {
            "mualliflar": Muallif.objects.all(),

        }
        return render(request, 'mualliflar.html', data)
    else:
        return render(request, 'muallif_qoshish.html')


def record_qosh(request):
    if request.method == "POST":
        talaba = request.POST.get("talaba")
        kitob = request.POST.get("kitob")
        admin = request.POST.get("admin")
        olingan_sana = request.POST.get("olingan_sana")
        qaytardi = True if request.POST.get("qaytardi") == 'on' else False
        Record.objects.create(talaba=talaba, kitob=kitob, admin=admin,
                              olingan_sana=olingan_sana, qaytardi=qaytardi)
        data = {
            "qaydlar": Record.objects.all(),

        }
        return render(request, 'record.html', data)
    else:
        return render(request, 'record_qoshish.html')


def admin_qosh(request):
    if request.method == "POST":
        ism = request.POST.get("talaba")
        ish_vaqti = request.POST.get("ish_vaqti")
        Admin.objects.create(ism=ism, ish_vaqti=ish_vaqti)
        data = {
            "adminlar": Admin.objects.all(),

        }
        return render(request, 'admin.html', data)
    else:
        return render(request, 'admin_qoshish.html')


def kitoblar(request):
    data = {
        "kitoblar": Kitob.objects.all()
    }
    return render(request, 'kitoblar.html', data)


def bitta_talaba(request, son):
    data = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, 'bitta_talaba.html', data)


def bitta_muallif(request, son):
    data = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, 'bitta_muallif.html', data)


def bitta_kitob(request, son):
    data = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request, 'bitta_kitob.html', data)


def bitta_record(request, son):
    data = {
        "qayd": Record.objects.get(id=son)
    }
    return render(request, 'bitta_record.html', data)
##########################################


def kitob_1(request):
    data = {
        "kitoblar": Kitob.objects.all().order_by("-sahifa")[0:3]
    }
    return render(request, 'sahifa.html', data)


def kitob_2(request):
    data = {
        "kitoblar": Kitob.objects.filter(janr="Badiiy")
    }
    return render(request, 'badiiy.html', data)


def kitob_4(request):
    data = {
        "kitoblar": Kitob.objects.filter(muallif__tirik=True),
        "xabar": "Barcha tirik mualliflar kitoblari"
    }
    return render(request, 'badiiy.html', data)


def kitob_3(request):
    data = {
        "kitoblar": Kitob.objects.filter(muallif__kitob_soni__lt=10)
    }
    return render(request, 'kitobi_oz.html', data)


def muallif_1(request):
    data = {
        "mualliflar": Muallif.objects.all().order_by("-kitob_soni")[0:3]
    }
    return render(request, 'kitob_soni.html', data)


def muallif_2(request):
    data = {
        "mualliflar": Muallif.objects.filter(tirik=True)
    }
    return render(request, 'tirik.html', data)


def record_1(request):
    data = {
        "qaydlar": Record.objects.all().order_by("-olingan_sana")[0:3]
    }
    return render(request, 'olingan_sana.html', data)


def record_2(request):
    data = {
        "qaydlar": Record.objects.filter(talaba__bitiruvchi=True),
        "xabar": "Bitiruvchi studentlarni qaydlari"
    }
    return render(request, 'olingan_sana.html', data)


def talaba_ochir(request, son):
    talaba = Talaba.objects.get(id=son)
    talaba.delete()
    return redirect('/talabalar')


def muallif_ochir(request, son):
    muallif = Muallif.objects.get(id=son)
    muallif.delete()
    return redirect('/mualliflar')


def record_ochir(request, son):
    record = Record.objects.get(id=son)
    record.delete()
    return redirect('/qaydlar')
