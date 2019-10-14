import csv

# We have an example csv file - "iris.csv"
# This file is seperated by commas, the default seperator for the csv module

# open file, we use `with` syntax so that the file is safely closed in case of an error
with open('csv/iris.csv') as irisfile:
    # csv.reader creates an iterator, 
    csvdata = csv.reader(irisfile)
    # that we can then iterate over using standard python `for` syntax
    # csv.reader isn't indexable, for more advanced usage, see pandas
    for row in csvdata:
        # Each `row` is a list of strings corresponding to a row in the csv file
        # our first row will be our headers
        # the next rows will be our data.
        print(row)


# Similarly, we can create a DictReader
with open('csv/iris.csv') as irisfile:
    # csv.DictReader creates an iterator, 
    csvdata = csv.DictReader(irisfile)
    # We can't index into dictreader either
    for row in csvdata:
        # every row is an ordered dict with the headers as keys, and data rows as values.
        print(row)


