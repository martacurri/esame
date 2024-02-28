#!/bin/bash

#Directory di destinazione per l'applicazione
directory='$HOME/Ait_esame_directory'


#Rpository GitHub
github_repository="https://github.com/MartaCurri/esame"

# Copia dei file dell'applicazione dalla repository GitHub nella directory di destinazione
echo "Clonazione del repository GitHub."
git clone "$github_repository" "$directory"

# Impostazione dei permessi di esecuzione per lo script di avvio
echo 'Impostazione dei permessi di esecuzione per lo script di avvio.'
chmod +x '$directory/ait_parte1.sh'

# Modifica del PythonPath e del PATH di sistema
echo "Modifica del PythonPath e del PATH di sistema."
echo "export PYTHONPATH=\$PYTHONPATH:$directory" >> ~/.bashrc
echo "export PATH=\$PATH:$directory" >> ~/.bashrc
source ~/.bashrc

echo "Installazione completata con successo."

