import deepl
import json

def translate_entire_json(file_path, target_lang, auth_key):
    # Load the JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Initialize the DeepL translator
    translator = deepl.Translator(auth_key)
    
    total_entries = len(data['events'])
    print(f"Total entries to translate: {total_entries}")
    
    # Translate each 'text' entry in 'events'
    for index, entry in enumerate(data['events'], start=1):
        if 'text' in entry:
            translated_text = translator.translate_text(entry['text'], target_lang=target_lang)
            entry['text'] = translated_text.text
            print(f"Translated entry {index}/{total_entries}")
    
    # Save the translated data back to a JSON file (if needed)
    with open("translated_test.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return data

# Parameters
auth_key = "123456789"  # Replace with actual DeepL Auth Key
target_lang = "KO"
file_path = "/Users/hotch/Downloads/test.json"  # Replace with the path to JSON file

# Execute the function
translated_data = translate_entire_json(file_path, target_lang, auth_key)
