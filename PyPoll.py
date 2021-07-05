# The data we need to retrive
# Reading data from the csv file
import csv
import os
file_to_load = os.path.join("./Resources", "election_results.csv")
with open(file_to_load) as election_data:

    # Print the file object
        #print(election_data)
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print each row in the csv file.
    #for row in file_reader:
     #   print(row)

    # Print the headers
    headers = next(file_reader)
    print(headers)
# Creating a filename vaiable to a direct or indirect path to the file.
    #file_to_save = os.path.join("analysis", "election_analysis.txt")
    #outfile = open(file_to_save, 'w')
# Write some data to the file.
    #outfile.write("Hello World")
     #outfile.write("--------------------\nArapahoe\nDenver\nJefferson")

# Close the file 
#outfile.close()
# 1. The total number of votes cast
# 2. The complete list of caditdates that received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each canditdate won.
# 5. The winner of the election based on popuar vote.
