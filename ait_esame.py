import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#VERIFICA PYTHON PARTE 1

nome_del_file = 'Nemo_6670.dat'
M_ass = [] #magnitudine
b_y = [] #indice colore-temperatura
age_parent_Gyr = [] #eta stelle

# Apre il file e legge i dati
with open(nome_del_file, 'r') as ppf:
    header = ppf.readline() # Salta l'intestazione
    for line in ppf:
        line = line.strip() 
        columns = line.split()
        
        M_ass.append(float(columns[4]))
        b_y.append(float(columns[8]))
        age_parent_Gyr.append(float(columns[12]))

age_bins = [0, 0.05, 0.11, 0.18, 0.25, 0.33, 0.41, 0.51, 0.61, 0.73, 0.85, 0.99, 1.14, 1.30, 1.40, 1.60, 1.89, 2.13, 2.39, 2.67, 2.99, 3.33, 3.70, 4.12, 4.57, 5.06, 5.60, 6.20, 6.85, 7.57, 8.35, 9.21, 10.15, 11.19, 12.52, 13.56]

#age_parent dentro age_bins
age_categorie = np.digitize(age_parent_Gyr, bins=age_bins)

#colore
cmap = plt.get_cmap('turbo')

#grandezza immagine
plt.figure(figsize=(13, 11))

for i, age_bin in enumerate(age_bins[:-1]):
    indices = np.where((age_categorie >= i + 1) & (age_categorie < i + 2))[0]
    plt.scatter(np.array(b_y)[indices], np.array(M_ass)[indices], c=cmap(i / (len(age_bins) - 1)), label=f'{age_bins[i]} Gyr-{age_bins[i+1]} Gyr', marker='*')
    

#inverto le assi
plt.gca().invert_yaxis()

plt.ylim(8.2, -4)
plt.xlim(-0.1, 1)

plt.xlabel('b_y')
plt.ylabel('M_ass')

plt.title('Diagramma colore - magnitudine', fontdict=None, loc='center', pad=None)

#grandezza legenda
plt.legend(fontsize='8')

plt.show()




#VERIFICA PYTHON PARTE 2

MsuH = [] #metallicita stelle
age_parent_Gyr = [] #eta stelle

# Apre il file e legge i dati
with open(nome_del_file, 'r') as ppf:
    header = ppf.readline() # Salta l'intestazione
    for line in ppf:
        line = line.strip() 
        columns = line.split()
        
        MsuH.append(float(columns[0]))
        age_parent_Gyr.append(float(columns[12]))


# Divido il campione in tre sotto-campioni in base all'età
age_bins = [0, 1, 5, 13.56]
labels = ['< 1 Gyr', '1-5 Gyr', '> 5 Gyr']

# Creo tre sotto-campioni di metallicità in base all'età
metallicita_subsets = [[] for _ in range(len(labels))]
for i, age in enumerate(age_parent_Gyr):
    if age < 1:
        metallicita_subsets[0].append(MsuH[i])
    elif 1 <= age < 5:
        metallicita_subsets[1].append(MsuH[i])
    else:
        metallicita_subsets[2].append(MsuH[i])

# Calcolo della media e della mediana delle tre distribuzioni di metallicità
media = [np.mean(subset) for subset in metallicita_subsets]
mediana = [np.median(subset) for subset in metallicita_subsets]

# Disegno gli istogrammi delle tre distribuzioni di metallicità
plt.figure(figsize=(10, 6))
colors = ['midnightblue', 'crimson', 'lime']
for i, subset in enumerate(metallicita_subsets):
    plt.hist(subset, bins=20, color=colors[i], alpha=0.5, label=labels[i])

# Aggiungo le medie e le mediane al grafico come linee verticali
for i in range(len(media)):
    plt.axvline(x=media[i], color=colors[i], linestyle='--', label=f'Media ({labels[i]}): {media[i]:.2f}')
    plt.axvline(x=mediana[i], color=colors[i], linestyle=':', label=f'Mediana ({labels[i]}): {mediana[i]:.2f}')

plt.xlabel('Metallicità (MsuH)')
plt.ylabel('Frequenza')

plt.title('Distribuzione delle metallicità stellari per le stelle nei tre sotto-campioni')

plt.legend()
plt.grid(True)

plt.show()




#VERIFICA PYTHON PARTE 3

MsuH = [] #metallicita stelle
m_ini = [] #massa iniziale stelle
age_parent_Gyr = [] #eta stelle

# Apre il file e legge i dati
with open(nome_del_file, 'r') as ppf:
    header = ppf.readline() # Salta l'intestazione
    for line in ppf:
        line = line.strip() 
        columns = line.split()
        
        MsuH.append(float(columns[0]))
        m_ini.append(float(columns[1]))
        age_parent_Gyr.append(float(columns[12]))


# Divido il campione in tre sotto-campioni in base all'età
age_bins = [0, 1, 5, 13.56]
labels = ['< 1 Gyr', '1-5 Gyr', '> 5 Gyr']

# Creo tre sotto-campioni di metallicità e massa in base all'età
metallicita_subsets = [[] for _ in range(len(labels))]
massa_subsets = [[] for _ in range(len(labels))]
for i, age in enumerate(age_parent_Gyr):
    if age < 1:
        metallicita_subsets[0].append(MsuH[i])
        massa_subsets[0].append(m_ini[i])
    elif 1 <= age < 5:
        metallicita_subsets[1].append(MsuH[i])
        massa_subsets[1].append(m_ini[i])
    else:
        metallicita_subsets[2].append(MsuH[i])
        massa_subsets[2].append(m_ini[i])

# Disegno i grafici a dispersione per ciascun campione
plt.figure(figsize=(10, 6))
colors = ['midnightblue', 'crimson', 'lime']
for i in range(len(labels)):
    plt.scatter(massa_subsets[i], metallicita_subsets[i], color=colors[i], alpha=0.5, label=labels[i])

plt.xlim(0,7)
plt.ylim(-2.5, 1)

plt.xlabel('Massa iniziale (m_ini)')
plt.ylabel('Metallicità (MsuH)')

plt.title('Metallicità in funzione della massa per i tre sotto-campioni')

#spostamento leggenda
plt.legend(loc='lower right')
plt.grid(True)

plt.show()


