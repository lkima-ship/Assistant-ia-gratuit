# sauvegarde ceci comme : create_structure.py
import os

# Structure des dossiers
structure = {
    '.github/workflows': ['deploy.yml'],
    'src/modules': ['__init__.py', 'ai_processor.py', 'email_handler.py', 
                   'calendar_manager.py', 'voice_processor.py', 'database.py'],
    'src/utils': ['__init__.py', 'config_loader.py', 'logger.py', 
                 'helpers.py', 'setup_wizard.py', 'backup.py'],
    'src/web/templates': ['base.html'],
    'src/api': ['__init__.py', 'routes.py', 'models.py'],
    'src/bots': ['telegram_bot.py', 'discord_bot.py'],
    'tests': ['__init__.py', 'test_ai.py', 'test_email.py', 'test_voice.py'],
    'docs': ['installation.md', 'usage.md', 'api.md', 'faq.md'],
    'scripts': ['install.sh', 'install.bat', 'setup.py'],
    'data/emails': [],
    'data/voice': [],
    'data/logs': [],
    'examples': ['basic_usage.py', 'custom_module.py'],
    'config': ['default.yaml', 'production.yaml'],
}

# Fichiers racine
root_files = [
    '.env.example', '.gitignore', 'requirements.txt', 'requirements-dev.txt',
    'Dockerfile', 'docker-compose.yml', 'railway.json', 'vercel.json',
    'fly.toml', 'render.yaml', 'pyproject.toml', 'setup.py', 'LICENSE', 'README.md'
]

# Fichiers src/
src_files = {
    'src': ['main.py', 'web_app.py', 'api_server.py'],
    'src/web': ['__init__.py', 'dashboard.py'],
}

print("🚀 Création de la structure...")

# Créer dossiers
for folder in structure:
    os.makedirs(f"assistant-ia-gratuit/{folder}", exist_ok=True)
    print(f"📁 Créé: assistant-ia-gratuit/{folder}")

# Créer fichiers dans dossiers
for folder, files in structure.items():
    for file in files:
        path = f"assistant-ia-gratuit/{folder}/{file}"
        with open(path, 'w', encoding='utf-8') as f:
            if file.endswith('.py'):
                f.write(f"# {file}\n")
            elif file.endswith('.md'):
                f.write(f"# {file.replace('.md', '')}\n")
        print(f"📄 Créé: {path}")

# Créer fichiers racine
for file in root_files:
    with open(f"assistant-ia-gratuit/{file}", 'w', encoding='utf-8') as f:
        f.write(f"# {file}\n")
    print(f"📄 Créé: assistant-ia-gratuit/{file}")

# Créer fichiers src/
for folder, files in src_files.items():
    for file in files:
        path = f"assistant-ia-gratuit/{folder}/{file}"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# {file}\n")
        print(f"📄 Créé: {path}")

print("\n✅ Structure créée avec succès!")
print("📁 Dossier: assistant-ia-gratuit/")
