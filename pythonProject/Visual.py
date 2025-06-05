import ast

import matplotlib.pyplot as plt
import CodeCheck
from CodeCheck import Errors

def return_graphs(file_data_list,path):
    all_file_names = []
    all_error_counts = []
    output_filenames = []

    for code, filename in file_data_list:
        if len(code.strip().splitlines()) > 200:
            file_too_long = 1
        else:
            file_too_long = 0

        tree = ast.parse(code)
        CodeCheck.add_parents(tree)
        check_code = CodeCheck.MyVisitor(code)
        check_code.errors[Errors.File_length_is_longer_then_200.value] = file_too_long

        hist_filename = f"{filename}_hist.png"
        print(f"datahist{filename}: {check_code.lengths}")
        create_histogram(check_code.lengths, path + "\\" + hist_filename)
        output_filenames.append(hist_filename)

        pie_filename = f"{filename}_pie.png"
        print(f"valuespie{filename}: {check_code.errors}")
        errors_without_0 = []
        errors_new = []
        for i in range(len(check_code.errors)):
            if check_code.errors[i] != 0:
                errors_without_0.append(check_code.errors[i])
                errors_new.append(Errors(i))
        create_pie_chart(errors_new, errors_without_0, path + "\\" + pie_filename)
        output_filenames.append(pie_filename)

        all_file_names.append(filename)
        all_error_counts.append(sum(check_code.errors))

    bar_filename = "Bar_Chart_All_Files.png"
    create_bar_chart(all_file_names, all_error_counts, path + "\\" + bar_filename)
    output_filenames.append(bar_filename)

    return output_filenames

def create_histogram(data, filename):
    plt.figure()
    plt.hist(data, bins=range(min(data), max(data)+2), color='blue', edgecolor='black', align='left')
    plt.title('Function lengths')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(filename)
    plt.close()

def create_pie_chart(labels, values, filename):
    plt.figure(figsize=(12, 6))
    plt.pie(values,labels=labels)
    plt.title('Number of issues per issue type')
    plt.savefig(filename)
    plt.close()

def create_bar_chart(file_names, error_counts, filename):
    for i in range(len(error_counts)):
        print(f"valuesbar{file_names[i]}: {error_counts[i]}")
    # print(f"Bar Chart - Files: {file_names}, Errors: {error_counts}")
    plt.figure()
    plt.bar(file_names, error_counts, color='green')
    plt.title('Number of issues per file')
    plt.xlabel('File Name')
    plt.ylabel('Number of Issues')
    plt.savefig(filename)
    plt.close()

def return_issues(code,filename):
    check_code = CodeCheck.MyVisitor(code)
    sum_all_errors = 0
    for item in check_code.errors:
        sum_all_errors += item
    if sum == 0:
        return f"The file: {filename} is written in a correct format."
    message = ""
    for i in range(len(check_code.errors)):
        if check_code.errors[i] == 1:
            message += f"You have {check_code.errors[i]} error of: {Errors(i).name.replace('_',' ')} \n"
        elif check_code.errors[i] > 1:
            message += f"You have {check_code.errors[i]} errors of: {Errors(i).name.replace('_', ' ')} \n"
    return message