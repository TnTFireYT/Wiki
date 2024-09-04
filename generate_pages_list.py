import os
import json

# Percorso della cartella dove si trovano le pagine
directory = './pages'

# Lista per memorizzare i percorsi delle pagine
pages_list = []

# Scansione della cartella per i file HTML
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        # Aggiungi il percorso relativo alla lista delle pagine
        pages_list.append(os.path.join(directory, filename))

# Genera un file JSON con l'elenco delle pagine
with open('pages_list.json', 'w') as json_file:
    json.dump(pages_list, json_file)

print(f'Elenco delle pagine generato con successo! {len(pages_list)} pagine trovate.')
