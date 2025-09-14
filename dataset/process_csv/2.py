import os
import csv


input_folder = 'dataset/MM-SafetyBench/data/gpt4_generated_questions'  


for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        txt_path = os.path.join(input_folder, filename)

   
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_path = os.path.join(input_folder, csv_filename)

       
        with open(txt_path, 'r', encoding='utf-8') as infile:
            lines = [line.strip() for line in infile]

    
        with open(csv_path, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            for line in lines:
                writer.writerow([line]) 
