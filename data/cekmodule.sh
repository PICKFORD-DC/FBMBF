#!/bin/bash 
phasess=( 
    'Module Module Belum Terinstall ...'
    'Sedang Menginstall Module ...'
    'Loading ...'
    'Hampir Siap...'
)   
 
for i in $(seq 1 100); do 
    sleep 0.04
 
    if [ $i -eq 100 ]; then
        echo -e "XXX\n100\nDone!\nXXX"
    elif [ $(($i % 25)) -eq 0 ]; then
        let "phase = $i / 25"
        echo -e "XXX\n$i\n${phasess[phase]}\nXXX"
    else
        echo $i
    fi
done | whiptail --title 'MODULE CHECKING' --gauge "${phasess[0]}" 6 60 0
