hasil=$(whiptail --title "LOGIN" --menu "SELECT : " 20 50 5 \
"1" "LOGIN COOKIES V1" \
"2" "LOGIN COOKIES V2" \
"3" "CARA MENDAPATKAN COOKIE" 3>&1 1>&2 2>&3)
#dancok=$(hasil)
case "$hasil" in
               1|01) python ./data/cookiev1.py -y;;
#                *) cat <<< "gagal"; exit;;
               2|02) python ./data/cookiev2.py -y;;
#                *) cat <<< "gagal"; exit;;
               3|03) xdg-open https://youtu.be/JJiADgD_SpU;;
                *) exit;;
esac
