# This is used to modify the header of .encase to suit the usage of Actran in lower versions
# Author: Memorised
# memorisexuxu@outlook.com
# Feel free to ask for many function, no matter in Chinese or English

# Function
In the script, several modifications were made to fit the Actran lower version
The data in element or node concerning scalar and vector is supported
Trim the data as you want. By default, the latest file is calculated by boolean trim_Import and trim_Import_Num
# Modified point:

# Specify the name of geometry by parameter geo_name
    model:  1   p****.geo   -->  model:  1   p00001.geo
# Delete the useless number 1 and the space
    scalar per node:  1  velocity_magnitude                               p****.scl1
    scalar per node:velocity_magnitude p****.scl1
# Usage:
It will open a file dialog, and you should select the file
After an Ahhh, the result with timeStamp is sit near the selected file

助力将Ensight转换成Actran能够读取的形式
