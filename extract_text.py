#
import re

import os

def extract_text_from_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Use regex to find all text within </ab> tags
        texts = re.findall(r'\">(.*?)</ab>', content)
        return texts

def main():
    base_path = os.path.dirname(os.path.realpath(__file__))
    target_folder = os.path.join(base_path, 'PodkorpusMilionowy')
    output_file_path = os.path.join(base_path, 'data.txt')
    file_count = 0

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(target_folder):
            for dir_name in dirs:
                xml_file_path = os.path.join(root, dir_name, 'text.xml')
                if os.path.exists(xml_file_path):
                    file_count += 1
                    texts = extract_text_from_xml(xml_file_path)
                    for text in texts:
                        output_file.write(f'"{text}"\n')
                        print(f'"{text}"')

    print(f"Liczba plików text.xml: {file_count}")

if __name__ == "__main__":
    main()


#Dane zaeksportowane
# * Autorów publikacji powołujących się na wyszukiwarkę PELCRA NKJP prosimy o cytowanie następującej publikacji:
#
# Piotr Pęzik (2012) Wyszukiwarka PELCRA dla danych NKJP. Narodowy Korpus Języka Polskiego. Przepiórkowski A., Bańko M., Górski R., Lewandowska-Tomaszczyk B. (red.). 2012. Wydawnictwo PWN .
