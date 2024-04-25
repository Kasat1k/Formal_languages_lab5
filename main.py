import re

pattern = r"^[a-zA-Z0-9\.]{4,10}[;:?]\d{2}\.\d{2}[;:?](\d{1,}[;:?])\d{4}[;:?](\d{2}\.\d{1}[;:?]\d{1}\.\d{2}[;:?])\d{2}[;:?]\d{2}[;:?]\d{2}\.\d{2}[;:?]\d{2}\.\d{2}$"

with open("input_file.txt", "r") as input_file:
    with open("output_file.txt", "w") as output_file:
        for line in input_file:
        
            line = re.sub(r'[:?]', ';', line)
           
            match = re.match(pattern, line)
            if match:
                groups = match.groups()
                # print("Groups found:", groups)
                new_line = re.sub(match.group(1), '', line)
                new_line = re.sub(match.group(2), '', new_line)
                output_file.write(new_line)
        print("Операція завершена. Результат збережено у файлі 'output_file.txt'.")



