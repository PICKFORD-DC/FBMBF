#!/usr/bin/env bash
nama=$(whiptail --title "Input Your Name" --inputbox "Masukan Nama Aseli Kamuh ☝️🗿" 8 40 3>&1 1>&2 2>&3)
echo -e "$nama" > ./data/.nama.txt
echo -e "SAYA $nama MENYETUJUI KEBIJAKAN FILE INI " > ./data/.pickfordganteng
whiptail --title "KEBIJAKAN" --yesno "Ini Adalah Tools Ilegal Jadi Jika Ada Masalah Pribadi Saat Menggunakan Tools Ini Saya Sebagai Author Tidak Bertanggung jawab! Jika Anda Memilih Yes Berarti Anda Menyetujui Kebijakan Kami" 20 50 
if [[ $? -eq 0 ]]; then 
  whiptail --title "MESSAGE" --msgbox "TERIMAKASIH ANDA TELAH MENYETUJUI KEBIJAKAN KAMI SEMOGA HOKI" 8 78 
elif [[ $? -eq 1 ]]; then 
  whiptail --title "MESSAGE" --msgbox "TERIMAKASIH ATAS KUNJUNGAN NYA" 8 78 
  rm ./data/.nama.txt ./data/.pickfordganteng
  exit
elif [[ $? -eq 255 ]]; then 
  whiptail --title "MESSAGE" --msgbox "TERIMAKASIH ATAS KUNJUNGAN NYA" 8 78 
fi 
