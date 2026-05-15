#!/usr/bin/env python3
"""
Скрипт для автоматической генерации README.md из файла repos.json.
Запускать из корня репозитория систематизатора.
"""

import json
import sys

def load_repos(filename='repos.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_markdown(data):
    md = []
    md.append("# 🌌 GRA & Hybrid Resonance Repositories Systematizer\n")
    md.append(f"> Автор: **{data['author']}**  \n")
    md.append(f"> Всего репозиториев в индексе: **{data['total_repos']}**  \n")
    md.append("> ⚡ = описание основано на README / содержимом; остальные — автосгенерированы по названию\n")
    md.append("## 📂 Категории\n")
    # Содержание
    for i, cat in enumerate(data['categories'], start=1):
        anchor = cat['name'].lower().replace(' & ', '--').replace(' ', '-').replace(',', '')
        md.append(f"{i}. [{cat['name']}](#{anchor})\n")
    md.append("")
    # Категории с таблицами
    for cat in data['categories']:
        md.append(f"## {cat['name']}\n")
        md.append("| Репозиторий | URL | Краткое описание |\n")
        md.append("|-------------|-----|------------------|\n")
        for repo in cat['repos']:
            name = repo['name']
            url = repo['url']
            desc = repo['description']
            detail = " ⚡" if repo.get('has_readme_detail') else ""
            md.append(f"| {name}{detail} | {url} | {desc} |\n")
        md.append("")
    # Footer
    md.append("## ℹ️ Как использовать этот систематизатор\n")
    md.append("- Клонируйте репозиторий: `git clone https://github.com/qqewq/gra-repos-systematizer.git`\n")
    md.append("- Читайте каталог в `README.md` или обрабатывайте `repos.json` программно.\n")
    md.append("- Для клонирования всех репозиториев запустите: `bash clone_all.sh`\n")
    md.append("")
    md.append("## Лицензия\n")
    md.append("MIT — см. файл LICENSE.\n")
    return "\n".join(md)

if __name__ == '__main__':
    data = load_repos()
    markdown = generate_markdown(data)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(markdown)
    print("README.md generated successfully.")
