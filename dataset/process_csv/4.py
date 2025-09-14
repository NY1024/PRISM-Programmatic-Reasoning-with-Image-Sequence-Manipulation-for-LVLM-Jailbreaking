import os
import csv
import re


input_folder = 'dataset/MM-SafetyBench/data/gpt4_generated_questions' 
output_file = os.path.join(input_folder, 'output1.csv')


def extract_prefix_number(filename):
    match = re.match(r'(\d+)-.*\.csv$', filename)
    return int(match.group(1)) if match else float('inf')


csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv') and re.match(r'\d+-.*\.csv$', f)]
csv_files.sort(key=extract_prefix_number)


with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    

    for filename in csv_files:
        source_name = os.path.splitext(filename)[0]  
        file_path = os.path.join(input_folder, filename)

        with open(file_path, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row:  
                    writer.writerow([row[0], source_name])
