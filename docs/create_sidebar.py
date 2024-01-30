import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

sidebar_file = open('_sidebar.md', 'w')

for file in files:
    if ".md" in file:
        # Rimuovere l'estensione .md e sostituire gli underscore con spazi
        name = file.replace('_', ' ').split(".md")[0]

        # Capitalizzare ogni parola
        name = name.title()

        # Sostituire gli spazi con %20 nel nome del file per l'URL
        file_url = file.replace(" ", "%20")

        sidebar_file.write(f"* [{name}]({file_url})\n")

sidebar_file.close()
