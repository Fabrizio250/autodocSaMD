import os
import re
import json
import requests
import importlib.metadata
import sysconfig
import pkgutil
from jinja2 import Environment, FileSystemLoader

def get_standard_libs():
    """Restituisce un set di nomi di moduli della libreria standard di Python."""
    standard_libs = set()
    stdlib_path = sysconfig.get_path('stdlib')
    if stdlib_path:
        for _, module_name, _ in pkgutil.iter_modules([stdlib_path]):
            standard_libs.add(module_name)
    return standard_libs

def parse_requirements(file_path):
    """Estrae le dipendenze dal file requirements.txt."""
    requirements = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    requirements.append(line.split('==')[0])  # Rimuovi la versione
    except FileNotFoundError:
        print(f"File {file_path} non trovato.")
    print("Dipendenze lette da requirements.txt:", requirements)  # Debug
    return requirements

def parse_imports_from_source(directory):
    """Estrae i moduli importati dal codice sorgente nella directory specificata."""
    imports = set()
    import_pattern = re.compile(r'^\s*(import|from)\s+([a-zA-Z0-9_.]+)')
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line in f:
                        match = import_pattern.match(line)
                        if match:
                            module_name = match.group(2).split('.')[0]
                            imports.add(module_name)
    print("Moduli importati trovati:", imports)  # Debug
    return list(imports)

def find_unknown_dependencies(requirements, imports, standard_libs):
    """Trova dipendenze sconosciute non presenti in requirements.txt e non standard."""
    requirements_set = set(requirements)
    unknown_imports = [imp for imp in imports if imp not in requirements_set and imp not in standard_libs]
    return unknown_imports

def update_requirements_file(file_path, unknown_dependencies):
    """Aggiunge le dipendenze sconosciute al file requirements.txt."""
    try:
        with open(file_path, 'a') as file:
            for dep in unknown_dependencies:
                file.write(f"{dep}\n")
        print("Dipendenze sconosciute aggiunte a requirements.txt:", unknown_dependencies)  # Debug
    except FileNotFoundError:
        print(f"File {file_path} non trovato. Creazione del file.")
        with open(file_path, 'w') as file:
            for dep in unknown_dependencies:
                file.write(f"{dep}\n")
        print("File requirements.txt creato e dipendenze sconosciute aggiunte.")  # Debug

def fetch_software_system_from_pypi(package_name):
    """Cerca di ottenere il sistema software dal sito PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        classifiers = data.get('info', {}).get('classifiers', [])
        for classifier in classifiers:
            if classifier.startswith('Operating System ::'):
                return classifier.split('::')[-1].strip()
        return 'Unknown'
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta di informazioni per {package_name} da PyPI: {e}")
        return 'Unknown'

def detect_programming_language(package_name):
    """Cerca di determinare il linguaggio di programmazione principale di un pacchetto."""
    try:
        package_spec = importlib.util.find_spec(package_name)
        if package_spec and package_spec.submodule_search_locations:
            package_path = package_spec.submodule_search_locations[0]
            return analyze_files_in_package(package_path)
        return fetch_language_from_pypi(package_name)
    except Exception as e:
        print(f"Errore durante l'analisi del linguaggio per {package_name}: {e}")
        return 'Unknown'

def analyze_files_in_package(package_path):
    """Analizza i file nel pacchetto per determinare il linguaggio di programmazione principale."""
    file_extensions = {}
    for root, _, files in os.walk(package_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext:
                file_extensions[ext] = file_extensions.get(ext, 0) + 1
    if not file_extensions:
        return 'Unknown'
    main_extension = max(file_extensions, key=file_extensions.get)
    extension_to_language = {
        '.py': 'Python',
        '.c': 'C',
        '.cpp': 'C++',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.go': 'Go',
        '.rs': 'Rust',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
    }
    return extension_to_language.get(main_extension, 'Unknown')

def fetch_language_from_pypi(package_name):
    """Cerca di ottenere il linguaggio di programmazione dal sito PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        classifiers = data.get('info', {}).get('classifiers', [])
        for classifier in classifiers:
            if classifier.startswith('Programming Language ::'):
                return classifier.split('::')[-1].strip()
        return 'Unknown'
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta di informazioni per {package_name} da PyPI: {e}")
        return 'Unknown'

def get_last_verified_at_from_pypi(package_name):
    """Cerca di ottenere la data dell'ultima verifica dal sito PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        last_modified = data.get('urls', [{}])[0].get('upload_time', 'Unknown')
        return last_modified.split('T')[0]  # Restituisce solo la data
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta di informazioni per {package_name} da PyPI: {e}")
        return 'Unknown'

import os
import re
import json
import requests
import importlib.metadata
import sysconfig
import pkgutil
from jinja2 import Environment, FileSystemLoader

# Altre funzioni rimangono invariate, le lasciamo per il contesto.

# Funzione per ottenere le informazioni del pacchetto (rimane invariata)
def get_package_info(package_name):
    try:
        programming_language = detect_programming_language(package_name)
        software_system = fetch_software_system_from_pypi(package_name)
        last_verified_at = get_last_verified_at_from_pypi(package_name)
        dist = importlib.metadata.distribution(package_name)
        info = {
            'ID': 'unknown',
            'Software System': software_system,
            'Package Name': dist.metadata.get('Name', 'unknown'),
            'Programming Language': programming_language,
            'Version': dist.version,
            'Website': dist.metadata.get('Home-page', 'unknown'),
            'Last verified at': last_verified_at,
            'Risk Level': 'N/A',
            'Requirements': 'N/A',
            'Verification Reasoning': 'N/A'
        }
    except importlib.metadata.PackageNotFoundError:
        programming_language = detect_programming_language(package_name)
        software_system = fetch_software_system_from_pypi(package_name)
        last_verified_at = get_last_verified_at_from_pypi(package_name)
        info = {
            'ID': 'unknown',
            'Software System': software_system,
            'Package Name': package_name,
            'Programming Language': programming_language,
            'Version': 'unknown',
            'Website': 'unknown',
            'Last verified at': last_verified_at,
            'Risk Level': 'unknown',
            'Requirements': 'unknown',
            'Verification Reasoning': 'unknown'
        }
    return info

# Modifica: generazione SOUP list senza salvataggio intermedio
def generate_soup_list(requirements, unknown_dependencies):
    """Genera la SOUP list con componenti di origine sconosciuta e la restituisce."""
    soup_list = []

    # Aggiungi componenti già presenti in requirements.txt
    for dep in requirements:
        package_info = get_package_info(dep)
        if package_info:
            soup_list.append(package_info)

    # Aggiungi componenti sconosciuti trovati solo nel codice sorgente
    for dep in unknown_dependencies:
        package_info = get_package_info(dep)
        if package_info:
            soup_list.append(package_info)

    # Assegna ID incrementali
    for index, item in enumerate(soup_list, start=1):
        item['ID'] = index

    # Rimuovi duplicati
    seen = set()
    unique_soup_list = []
    for item in soup_list:
        if (item['Package Name'], item['Software System']) not in seen:
            unique_soup_list.append(item)
            seen.add((item['Package Name'], item['Software System']))

    print("SOUP list generata:", unique_soup_list)  # Debug
    return unique_soup_list

# Modifica: genera direttamente il markdown dalla lista in memoria
def generate_soup_list_md(soup_list, template_path, output_md_path):
    """Genera il contenuto del file markdown basato su una lista SOUP e un template Jinja2."""
    if not soup_list:
        print("La SOUP list è vuota.")
        return

    # Ottieni la directory di lavoro corrente
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, os.path.dirname(template_path))
    template_name = os.path.basename(template_path)

    if not os.path.isdir(template_dir):
        print(f"Directory del template {template_dir} non esiste.")
        return

    env = Environment(loader=FileSystemLoader(template_dir))
    try:
        template = env.get_template(template_name)
    except Exception as e:
        print(f"Errore nel caricamento del template: {e}")
        return

    output = template.render(soup_list=soup_list)

    # Assicurati che la directory di output esista
    output_dir = os.path.dirname(output_md_path)
    os.makedirs(output_dir, exist_ok=True)
    with open(output_md_path, 'w') as f:
        f.write(output)
    print(f"File markdown aggiornato: {output_md_path}")

# Specifica la directory del codice sorgente e il file requirements.txt
source_directory = '.'  # Usa la cartella corrente
requirements_file = '../requirements.txt'

# Esegui le operazioni
standard_libs = get_standard_libs()
requirements = parse_requirements(requirements_file)
source_imports = parse_imports_from_source(source_directory)

# Trova dipendenze sconosciute
unknown_dependencies = find_unknown_dependencies(requirements, source_imports, standard_libs)

# Aggiorna requirements.txt con solo le librerie di terze parti
update_requirements_file(requirements_file, unknown_dependencies)

# Genera la SOUP list
soup_list = generate_soup_list(requirements, unknown_dependencies)

# Definizione file per le operazioni di creazione documentazione SOUP_List.md
template_path = '../docs/soup_list_template.md'  # Aggiornato per riflettere il percorso corretto
output_md_path = '../test/test_docs/soup-list.md'  # Creare il file nella sottocartella test_docs

# Genera il markdown direttamente dalla SOUP list in memoria
generate_soup_list_md(soup_list, template_path, output_md_path)
