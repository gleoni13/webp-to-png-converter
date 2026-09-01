import os
from PIL import Image

# Ottiene la cartella in cui si trova questo script
cartella_corrente = os.path.dirname(os.path.abspath(__file__))

# Cambia la directory di lavoro del terminale su quella dello script
os.chdir(cartella_corrente)

conteggio = 0

# Cicla tutti i file nella cartella
for file in os.listdir('.'):
    if file.lower().endswith('.webp'):
        # Apri l'immagine WebP
        img = Image.open(file)
        
        # Genera il nuovo nome sostituendo l'estensione
        nome_png = os.path.splitext(file)[0] + '.png'
        
        # Salva in formato PNG
        img.save(nome_png, 'PNG')
        conteggio += 1
        print(f"Convertito: {file} -> {nome_png}")

print(f"\nFatto! Convertite con successo {conteggio} immagini.")