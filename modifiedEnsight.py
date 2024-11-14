# This is used to modify the header of .encase to suit the usage of Actran in lower versions
# Author: Memorised
# memorisexuxu@outlook.com
# Feel free to ask for many function, no matter in Chinese or English

# Function
# In the script, several modifications were made to fit the Actran lower version
# The data in element or node concerning scalar and vector is supported
# Trim the data as you want. By default, the latest file is calculated by boolean trim_Import and trim_Import_Num
# Modified point:
"""
# Specify the name of geometry by parameter geo_name
    model:  1   p****.geo   -->  model:  1   p00001.geo
# Delete the useless number 1 and the space
    scalar per node:  1  velocity_magnitude                               p****.scl1
    scalar per node:velocity_magnitude p****.scl1
# Usage:
#
# It will open a file dialog, and you should select the file
# After an Ahhh, the result with timeStamp is sit near the selected file
"""

import os
import re
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Pre-defined variables
geo_name = f"ps00001.geo"
files_needed_to_import = 10
trim_Import = True
trim_Import_Num = 20  # Default latest
#
## Program
# Define the path to the .encase file
root = tk.Tk()
root.withdraw()
filetypes = [("ENCAS files", "*.encas")]
obtain_file_dir = filedialog.askopenfilename(filetypes=filetypes)
directory, file_with_extension = os.path.split(obtain_file_dir)
os.chdir(directory)
# obtain_file_dir = r"C:\Users\XUXUEPYC\Desktop\p.encas"
if obtain_file_dir:
    if trim_Import:
        print("Warning: Running in TRIM mode!!!")
    trim_Import  # Read the content of the selected file
    with open(obtain_file_dir, "r") as file:
        lines = file.readlines()
        num_lines = len(lines)
    # Remove comments from the fileProcess the text format content
    result = ""
    data = {}
    capturing = False
    current_key = None

    for index in range(num_lines - 2):

        header = lines[index].strip().split(":", 1)[0]

        if lines[index].strip().upper() in ["FORMAT", "GEOMETRY", "VARIABLE", "TIME"]:
            data[index] = lines[index].strip()

        elif header.upper() == "MODEL":
            data[index] = "model:" + geo_name

        elif header in [
            "scalar per element",
            "scalar per node",
            "vector per element",
            "vector per node",
        ]:
            variale = lines[index].split(":", 1)[1].strip().split()[1]
            variabel_file = lines[index].split(":", 1)[1].strip().split()[2]
            data[index] = header + ":" + variale + " " + variabel_file

        elif header == "time set":
            data[index] = (
                header + ":" + lines[index].split(":", 1)[1].strip().split()[0]
            )

        elif header == "number of steps":
            if trim_Import:
                data[index] = header + ":" + str(trim_Import_Num)

        elif header == "time values":
            if trim_Import:
                time_mark_index = index
                time_series = lines[time_mark_index].split(":", 1)[1]
                for time_loop_index in range(time_mark_index, num_lines - 3):
                    time_series = "".join(
                        ["".join([time_series, lines[time_loop_index + 1]])]
                    )
                data[time_mark_index] = header + ":"
                for value in time_series.split()[-trim_Import_Num:]:
                    data[time_mark_index + 1] = value
                    time_mark_index += 1
                break
            else:
                time_mark_index = index
                time_series = lines[time_mark_index].split(":", 1)[1]
                for time_loop_index in range(time_mark_index, num_lines - 3):
                    time_series = "".join(
                        ["".join([time_series, lines[time_loop_index + 1]])]
                    )
                data[time_mark_index] = header + ":"
                for value in time_series.split():
                    data[time_mark_index + 1] = value
                    time_mark_index += 1
                    # print(value)
                break
        else:
            data[index] = lines[index].strip()
else:
    print("No file selected.")

current_time = datetime.now()
formatted_time = current_time.strftime("%m%d_%H%M")
output_file = file_with_extension.split(".")[0] + "_" + formatted_time + ".encase"
with open(output_file, "w") as f:
    for header, value in data.items():
        f.write(f"{value}\n")
    print("Done")
    print(f"File saved in {output_file}")

root.destroy()
