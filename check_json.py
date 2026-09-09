import json
import os
import re

files = [
    'history_literature.json', 'history_movies.json', 'deep_dive_articles.json',
    'history_quiz_sets.json', 'history_glossary.json', 'history_literature_en.json',
    'history_movies_en.json', 'deep_dive_articles_en.json'
]

out = open('json_issues.txt', 'w', encoding='utf-8')
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        try:
            content = file.read()
            data = json.loads(content)
            
            def check_dict(d, path=""):
                if isinstance(d, dict):
                    for k, v in d.items():
                        check_dict(v, path + "." + k)
                elif isinstance(d, list):
                    for i, v in enumerate(d):
                        check_dict(v, path + f"[{i}]")
                elif isinstance(d, str):
                    if d.strip() == "":
                        out.write(f"{f}: Empty string at {path}\n")
                    if "Lorem" in d or "lorem ipsum" in d:
                        out.write(f"{f}: Lorem ipsum at {path}\n")
                    if "TODO" in d or "FIXME" in d:
                        out.write(f"{f}: TODO/FIXME at {path}\n")
            check_dict(data)
        except Exception as e:
            out.write(f"Error reading {f}: {e}\n")
out.close()
