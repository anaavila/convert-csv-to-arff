# convert-csv-to-arff
Simple Python program that converts a comma separated value (CSV) files to Attribute-Relation File Format (ARFF).
where 'converts' means that an arff file is created and populated with the csv data. 
The csv file is not deleted or modified.

What the program does:
Reads a csv file, selects all its attributes and assigns its data type ("numeric" or "nominal").
Selects unique data values for each nominal attribute, and inserts a '0' on each empty cell.

This program was made to facilitate some csv data cleaning when I was trying to open a csv file with Weka. 
This program helps to clean the csv file by converting it to arff format when the csv file has some inconsistencies, 
such as having numeric and nominal values for the same attribute values, and when it has empty cells.


About the ARFF format and the Weka Software:
ARFF file format is used with Weka, a machine learning software from the
University of Waikato. Information about the ARFF file and Weka is on the
University of Waikato website: https://www.cs.waikato.ac.nz/ml/weka/arff.html


How to use the program:
- Need Python 3.6
- On program lines 34, 35, and 36, add the information of the csv file name 
you want to convert to arff format, what name you want to give it once converted
to arff, and what name you want to give to your relation.

You can play around with the .csv file I included, and see its outcome on the .arff
file included as well.

Note:
You can open the arff file with a text editor
