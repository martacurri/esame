#!/bin/bash

# Definisci il percorso completo della cartella di destinazione
destination_folder="$HOME/Desktop/Directory_esame"

# Utilizza il percorso completo della cartella di destinazione con il nome del file nella richiesta wget
wget -P "$destination_folder" https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat

if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAULT
fi

# Ottieni il percorso completo del file scaricato
downloaded_file="$destination_folder/Nemo_6670.dat"

# Verifica se il file è stato scaricato correttamente
if [ -e "$downloaded_file" ]
    then
        echo "Il file è stato scaricato correttamente."
    else
        echo "Errore durante il download del file."
        exit 1
fi

# Utilizza il percorso completo del file scaricato come variabile di ambiente
export DATA_FILE_PATH="$downloaded_file"
echo "Percorso del file scaricato: $DATA_FILE_PATH"

# Esegui il tuo script Python passando il percorso del file come argomento
python3 ait_esame.py "$HOME/Desktop/Directory_esame"

# Verifica lo stato di uscita dello script Python
if [ $? -eq 0 ]
    then
        echo "Lo script Python ha completato l'esecuzione con successo."
    else
        echo "Errore durante l'esecuzione dello script Python."
fi

