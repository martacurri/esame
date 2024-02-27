#!/bin/bash

wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
if [ $? -eq 0 ]
    then 
        echo OK
    else 
        echo FAULT
fi
ls -l Nemo_6670.dat

export DATA_FILE_PATH='pwd'/Nemo_6670.dat
echo $DATA_FILE_PATH

python3 ait_esame.py "$DATA_FILE_PATH"
  
# Verifica dello stato di uscita dello script di risoluzione
if [ $? -eq 0 ]
    then
        echo "Lo script di risoluzione ha completato l'esecuzione con successo."
    else
        echo "Errore durante l'esecuzione dello script di risoluzione."
fi

