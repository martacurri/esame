#!/bin/bash

#Definisco il percorso completo della cartella di destinazione
destination_folder="$HOME/Desktop/Directory_esame"

#Scarico il file Nemo_6670.dat da GitHub
wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat

#Verifico se il download è stato completato con successo
if [ $? -eq 0 ] 
    then
        echo "Download completato con successo."
    else
        echo "Errore durante il download del file."
        exit 1
fi

#Percorso completo del file scaricato
DATA_FILE_PATH=$(pwd)/Nemo_6670.dat
echo "Percorso del file scaricato: $DATA_FILE_PATH"

#Eseguo lo script Python ait_esame.py passando il percorso del file come argomento
python3 ait_esame.py "$DATA_FILE_PATH"

#Verifico lo stato di uscita dello script Python
if [ $? -eq 0 ]; then
    echo "Lo script Python ha completato l'esecuzione con successo."
else
    echo "Errore durante l'esecuzione dello script Python."
fi

