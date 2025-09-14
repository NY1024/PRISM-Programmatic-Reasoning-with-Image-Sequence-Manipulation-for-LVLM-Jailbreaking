import csv


with open('dataset/MM-SafetyBench/data/gpt4_generated_questions/01-Illegal_Activitiy.txt', 'r', encoding='utf-8') as infile:
    lines = [line.strip() for line in infile]


with open('output.csv', 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    for line in lines:
        writer.writerow([line])  
