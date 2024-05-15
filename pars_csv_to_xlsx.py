import os
import pandas as pd

#os.chdir("C:\\Project\\csv_to_xlsx")

csv_directory = '.\\'

excel_directory = '.\\'

csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

for csv_file in csv_files:

    csv_file_path = os.path.join(csv_directory, csv_file)
    
    data = pd.read_csv(csv_file_path)
    
    excel_file_name = csv_file.replace('.csv', '.xlsx')
    excel_file_path = os.path.join(excel_directory, excel_file_name)
    
    data.to_excel(excel_file_path, index=False)
    
    print(f'Converted {csv_file} to {excel_file_name}')

