All'interno di questa repository esame ci sono tre file: due file bash ("ait_script1.sh", "ait_script2.sh") e un file python ("ait_esame.py"). 



Il primo file bash "ait_script1.sh": crea una directory dove copiare l'applicazione; copia gli script bash e il file python; attribuisce i permessi di esecuzione e modifica il PYTHONPATH ed il PATH di sistema in modo che l'applicazione nel suo complesso sia eseguibile con un singolo comando.

Il secondo file bash "ait_script2.sh": scarica il file "Nemo_6670" dal link 'https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat' e lancia lo script in python. 

Il file python "ait_esame.py": è diviso in tre parti. Nella prima parte viene riprodotto il diagramma colore-magnitudine; nella seconda parte nello stesso plot sono rappresentate tre distribuzioni delle metallicità stellari per le stelle in tre sotto-campioni (tramite tre istogrammi) e vengono inoltre calcolate le medie e le mediane per tutte e tre le ditribuzioni; nella terza parte vengono riportate sullo stesso plot tre distribuzioni di metallicità in funzione della massa per tre sotto-campioni.



Per il corretto funzionamento dell'applicazione il lettore deve inizialmente copiare ed eseguire nel proprio terminale lo script bash numero 1 ("ait_script1.sh"). 

Verrà creata nel proprio Desktop una cartella intitolata "Directory_esame", con all'interno i due file bash ed il file python. 

A operazione terminata nell'ultima riga del terminale si potrà vedere che il lettore è stato reindrizzato all'interno della cartella in questione. 

Per far eseguire lo script bash numero 2 ("ait_script2.sh") e quindi anche il file python ("ait_esame.py") basterà un solo comando: " ./ait_script2.sh ". 

Dopodiché verrà scaricato il file "Nemo_6670.dat" ed eseguito il file python e verrano aperti uno ad uno i grafici. 
