# Converts comma separated value (CSV) files 
# to Attribute-Relation File Format (ARFF).
# where 'converts' means that an arff file is created and populated with
# the csv data. The csv file is not deleted or modified.
#
# @Author Ana Avila - github.com/anaavila
# @Date December, 2016 - January, 2017
#
# Python 3.6
#
# @Description
# Simple python program that reads a csv file, selects all its attributes 
# and assigns its data type ("numeric" or "nominal").
# Selects unique data values for each nominal attribute, and 
# inserts a '0' on each empty cell.
#
# This program was made to facilitate some csv data cleaning when I was
# trying to open a csv file in Weka, for a school research project.
# This program helps to clean the csv file by converting it to arff format
# when the csv file has some inconsistencies, such as having numeric and 
# nominal values for the same attribute values, and when it has empty cells.
#
# @About the ARFF format and Weka Software
# ARFF file format is used with Weka, a machine learning software from the
# University of Waikato. Information about the ARFF file and Weka is on the
# University of Waikato website: https://www.cs.waikato.ac.nz/ml/weka/arff.html
#
#
# Note:
# You can open the arff file with a text editor
#

import csv
import os

fileToRead = "worldcup2014.csv"  #csv file name or absolute path to be open.
fileToWrite = "worldcup2014.arff" #name as how you'll save your arff file.
relation = "World Cup 2014" #how you'll like to call your relation as.

dataType = [] # Stores data types 'nominal' and 'numeric'
columnsTemp = [] # Temporary stores each column of csv file except the attributes
uniqueTemp = [] # Temporary Stores each data cell unique of each column
uniqueOfColumn = [] # Stores each data cell unique of each column
dataTypeTemp = [] # Temporary stores the data type for cells on each column
finalDataType = [] # Finally stores data types 'nominal' and 'numeric'
attTypes = [] # Stores data type 'numeric' and nominal data for attributes
p = 0 # pointer for each cell of csv file

writeFile = open(fileToWrite, 'w')

#Opening and Reading a CSV file
f = open(fileToRead, 'r')
reader = csv.reader(f)
allData = list(reader)
attributes = allData[0]
totalCols = len(attributes)
totalRows = len(allData)
f.close()

# Add a '0' for each empty cell
for j in range(0,totalCols):
	for i in range(0,totalRows):
		if 0 == len(allData[i][j]):
			allData[i][j] = "0"

# check for comams or blanks and adds single quotes
for j in range(0,totalCols):
	for i in range(1,totalRows):
		allData[i][j] = allData[i][j].lower()
		if "\r" in allData[i][j] or '\r' in allData[i][j] or "\n" in allData[i][j] or '\n' in allData[i][j]:
			allData[i][j] = allData[i][j].rstrip(os.linesep)
			allData[i][j] = allData[i][j].rstrip("\n")
			allData[i][j] = allData[i][j].rstrip("\r")
		try:
			if allData[i][j] == str(float(allData[i][j])) or allData[i][j] == str(int(allData[i][j])):
				print
		except ValueError as e:
				allData[i][j] = "'" + allData[i][j] + "'"

# fin gives unique cells for nominal and numeric
for j in range(0,totalCols):
	for i in range(1,totalRows):
		columnsTemp.append(allData[i][j])
	for item in columnsTemp:
		if not (item in uniqueTemp):
			uniqueTemp.append(item)
	uniqueOfColumn.append("{" + ','.join(uniqueTemp) + "}") 
	uniqueTemp = []
	columnsTemp = []

# Assigns numeric or nominal to each cell
for j in range(1,totalRows):
	for i in range(0,totalCols):
		try:
			if allData[j][i] == str(float(allData[j][i])) or allData[j][i] == str(int(allData[j][i])):
				dataType.append("numeric")
		except ValueError as e:
				dataType.append("nominal")

for j in range(0,totalCols): 
	p = j
	for i in range(0,(totalRows-1)): 
		dataTypeTemp.append(dataType[p])
		p += totalCols  
	if "nominal" in dataTypeTemp:
		finalDataType .append("nominal")
	else:
		finalDataType .append("numeric")
	dataTypeTemp = []

for i in range(0,len(finalDataType )):
	if finalDataType [i] == "nominal":
		attTypes.append(uniqueOfColumn[i])
	else:
		attTypes.append(finalDataType[i])

# Show comments
writeFile.write("%\n% Comments go after a '%' sign.\n%\n")
writeFile.write("%\n% Relation: " + relation +"\n%\n%\n")
writeFile.write("% Attributes: " + str(totalCols) + " "*5 
	+ "Instances: " + str(totalRows-1) + "\n%\n%\n\n")

# Show Relation
writeFile.write("@relation " + relation + "\n\n")

# Show Attributes
for i in range(0,totalCols):
	writeFile.write("@attribute" + " '" + attributes[i] 
		+ "' " + attTypes[i] + "\n")

# Show Data
writeFile.write("\n@data\n")
for i in range(1,totalRows):
	writeFile.write(','.join(allData[i])+"\n")

print(fileToWrite + " was converted to " + fileToRead)
