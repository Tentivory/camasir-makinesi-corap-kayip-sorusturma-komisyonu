#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çamaşır Makinesi Çorap Kayıp Soruşturma Komisyonu
Resmi Protokol v1.0 — Çalışır. Gerçekten. Çorap hâlâ kayıptır.
"""

import random
import datetime

SANIKLAR = [
    "çamaşır makinesi tamburu",
    "kurutma programının 3. dakikası",
    "esrarengiz lastik conta",
    "komşunun balkonundaki güvercin",
    "çorabın kendi iradesi",
    "kızılötesi görünmezlik programı",
]

KARARLAR = [
    "Çorap geçici olarak kayıp ilan edilmiştir. Dosya açık kalacaktır.",
    "Makine şüpheli sıfatıyla dinlenmiştir. İfadesi yetersiz bulunmuştur.",
    "Tek kalan çorap resmi evlat edinilmiştir. Artık tek başına vatandaştır.",
    "Soruşturma derinleştirilmiştir. Derinleşme sonucu yine çorap bulunamamıştır.",
    "Komisyon oybirliğiyle kahve molasına gitmiştir. Çorap hâlâ yok.",
]

# gizli not: bazı çiftler yıkamanın sonunda da, sandığın sonunda da tek kalır.

def tutanak_uret(renk="siyah", desen="düz"):
    tarih = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    sanik = random.choice(SANIKLAR)
    karar = random.choice(KARARLAR)
    sicil = f"CRAP-{random.randint(10000, 99999)}"
    metin = f"""
============================================================
T.C. ÇAMAŞIR MAKİNESİ ÇORAP KAYIP SORUŞTURMA KOMİSYONU
Resmi Tutanak  —  {tarih}
Sicil No: {sicil}
============================================================
Konu     : {renk} renkli, {desen} desenli çorabın kaybı
Şüpheli : {sanik}
Karar    : {karar}
Not      : Çiftin diğer üyesi ifadesinde "ben girdim, o çıkmadı" demiştir.
============================================================
"""
    return metin.strip()


def main():
    print(tutanak_uret())
    print()
    print("Komisyon çalışmalarına devam etmektedir.")
    print("Lütfen makineyi kapatmayınız. Kanıt karartılabilir.")


if __name__ == "__main__":
    main()
