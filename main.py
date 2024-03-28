import numpy as np
import pandas as pd

#this is my project for python course
#Electro pi





def starting():
    while True:
        print("Write A to show the full data\nWrite B to show the removed Missing Values\nWrite C to show the Basic Statistics for the data\nWrite D to perform One-Hot Encoding for categorical columns\nWrite 'Leave' to stop")
        choice = input("Choose a number: ").lower()

        if choice == "a":
            print(file)
            starting()
            break

        elif choice == "b":
            removed_missing_values()
            starting()
            break


        elif choice == "c":
            Statistics()
            starting()
            break

        elif choice == "d":
            file_input = one_hot_encode_categorical_columns(file)
            print("One-Hot Encoding applied to categorical columns.")
            print(file_input)
            starting()
            break

        elif choice == "leave":
            break
        else:
            print("Invalid input. Please input one of the numbers.")
starting()

def check_file():
    name_of_the_file = input('put the file name here ')
    file_content = ''

    try:
        if name_of_the_file.find('.json') != -1:
            file_content = pd.read_json(name_of_the_file)

        elif name_of_the_file.find('.xlsx') != -1 or name_of_the_file.find('.xls') != -1:
            file_content = pd.read_excel(name_of_the_file)

        elif name_of_the_file.find('.csv') != -1:
            file_content = pd.read_csv(name_of_the_file)

        else:
            print("make sure if the file name is corrct")
            check_file()
        return file_content
    except:
        print("something went wrong")

file_input = check_file()


def removed_missing_values():
    global file_input
    while True:
        axis = input("Do you want to remove rows or columns? Type 'row' for rows or 'column' for columns: ").lower()

        if axis == 'row':
            print(file_input.dropna())
            break
        elif axis == 'column':
            print(file_input.dropna(axis=1))
            break
        else:
            print("Invalid axis. No changes made.")



def one_hot_encode_column(data, column_name):
    unique_values = data[column_name].unique()
    for value in unique_values:
        new_column_name = f"{column_name}_{value}"
        data[new_column_name] = (data[column_name] == value).astype(int)
    data = data.drop(column_name, axis=1)
    return data

def one_hot_encode_categorical_columns(data):
    categorical_columns = data.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        data = one_hot_encode_column(data, column)
    return data
file = file_input


def Statistics():
    print("Statistics:")
    file_mean = file_input.mean(numeric_only=True, skipna=True)
    print("The mean is" + file_mean)
    file_median = file_input.median(numeric_only=True)
    print("the Median is", file_median)
    file_std = file_input.std(numeric_only=True)
    print("the Standard Deviation is" + file_std)

