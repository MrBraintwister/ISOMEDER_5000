import os
import glob
import csv

def read_cell_values(file, cell_list):
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row_idx, row in enumerate(reader):
            for col_idx, cell in enumerate(row):
                if (row_idx + 1, col_idx + 1) in cell_list:
                    data.append(cell)
    return data

def main():
    csv_files = glob.glob('*.csv')
    cell_list = [(2, 2), (3, 2), (19, 2), (21, 2), (31, 3), (34, 3), (19, 3), (21, 3), (31, 4), (34, 4)]
    extracted_data = []

    for file in csv_files:
        file_data = read_cell_values(file, cell_list)
        correct_order_data = [
            file_data[0], file_data[1], file_data[2], file_data[4],
            file_data[6], file_data[8], file_data[3], file_data[5],
            file_data[7], file_data[9]
        ]
        extracted_data.append(correct_order_data)

    header = [
        "Name", "DB", "Side_1", "Speed_1", "Peak_Torque_flex_1",
        "Peak_Torque_ext_1", "Side_2", "Speed_2", "Peak_Torque_flex_2", "Peak_Torque_ext_2"
    ]

    with open('isomed_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(header)
        for row in extracted_data:
            writer.writerow(row)

if __name__ == '__main__':
    main()
