#!/bin/bash

#Directory di destinazione per l'applicazione
directory="$HOME/Desktop/Directory_esame"

#Creo la directory di destinazione se non esiste
mkdir -p "$directory"

#URL del repository GitHub
github_repository="https://github.com/MartaCurri/esame"

#Copia dei file dell'applicazione dalla repository GitHub nella directory di destinazione
echo "Clonazione del repository GitHub."
git clone "$github_repository" "$directory"

#Modifica del PythonPath e del PATH di sistema
echo "Modifica del PythonPath e del PATH di sistema."
echo "export PYTHONPATH=\$PYTHONPATH:$directory" >> ~/.bashrc
echo "export PATH=\$PATH:$directory" >> ~/.bashrc
source ~/.bashrc

#Impostazione dei permessi di esecuzione per lo script di avvio
echo "Impostazione dei permessi di esecuzione per lo script di avvio."
chmod +x "$directory/ait_script2.sh" 

echo "Installazione completata con successo."

#Entro nella directory giusta
cd "$directory"

