# MENU UTAMA
from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import menuKegiatan
import menuObat
import menuProfile
import menuTentangKami
import globalVar
import whatsapp

def menuUtama():
    while True:
        globalVar.printTitle("Menu Utama")
        print("[1] Obat")
        print("[2] Kegiatan")
        print("[3] Profile")
        print("[4] Tentang kami")
        print("[5] Logout\n")
        print("[w] Contact Person")
        print("=" * 32)

        masukkan_angka = input("> ")
        if masukkan_angka == "1":
            menuObat.menuObat()

        elif masukkan_angka == "2":
            menuKegiatan.menuKegiatan()

        elif masukkan_angka == "3":
            menuProfile.menuProfile()

        elif masukkan_angka == "4":
            menuTentangKami.menuTentangKami()
            
        elif masukkan_angka == "5":
            globalVar.status_login = False
            globalVar.nomor_induk_mahasiswa = None
            globalVar.list_data = []
            break
        elif masukkan_angka.lower() == "w":
            whatsapp.buka_whatsapp()
        else:
            globalVar.inputanInvalid()