import time
import os
# from datetime import datetime, timedelta


# def hitung_timer():
#     input_jam = input("HH:MM:SS ")

#     try:
#         # Waktu target
#         waktu = datetime.strptime(input_jam, "%H:%M:%S")

#         # Waktu sekarang
#         waktu_now = datetime.now()

#         # Selisih waktu
#         selisih_waktu = waktu - waktu_now
#         selisih_jam = selisih_waktu.seconds // 3600
#         selisih_menit = (selisih_waktu.seconds % 3600) // 60
#         selisih_detik = selisih_waktu.seconds % 60
#         while True:
#             if selisih_detik != 0:
#                 selisih_detik -= 1
#             elif selisih_detik == 0:
#                 selisih_detik = 60
#                 selisih_menit -= 1
#             elif selisih_menit == 0:
#                 selisih_menit = 60
#                 selisih_jam -= 1
#             elif selisih_jam == 0 and selisih_menit == 0 and selisih_detik == 0:
#                     print("waktu habis")
#                     break
#             print(f"{selisih_jam}:{selisih_menit}:{selisih_detik}")
#             time.sleep(1)
#             os.system("cls")



#         # Selisih waktu
#         # selisih_jam = jam_target - jam_now
#         # selisih_menit = menit_target - menit_now
#         # selisih_detik = detik_target = detik_now
#         # print(f"{selisih_jam}:{selisih_menit}:{selisih_detik}")
#         # while True:
#         #     if detik_target == 0:
#         #         detik_target = 60
#         #         menit_target -= 1
#         #     elif detik_target != 0:
#         #         detik_target -= 1
    
#     except ValueError:
#         print("Format tidak valid")


# hitung_timer()
        


#         # # Memeriksa apakah sudah mencapai atau melebihi jam tujuan
#         # if selisih_waktu.total_seconds() <= 0:
#         #     print("\nWaktu tujuan telah tercapai. Selamat!")
#         #     break


username = input("Masukan username: ")
password = input("Masukan password: ")
kesempatan = 4
while True:
    if username == "rocky" and password == "123456":
        print("Selamat Datang!")
        break
    else:
        print("Something wrong\n")
        kesempatan -= 1
        print(f"Kesempatan Anda {kesempatan} kali lagi")
        time.sleep(1)
        os.system("cls")
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        if kesempatan == 1:
            print("Anda gagal melkukan login")
            break