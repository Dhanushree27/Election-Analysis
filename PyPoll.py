'''
#Total number of votes cast
#Open the File and store the information in an array
#Calculate the total number of ballot IDs
#Store the information in a field

#A complete list of candidates who received votes
#Take the array
#Calculate the unique values in Candidate ID field and store it in a dictionary

#Total number of votes each candidate received
#Take the array
#Calculate the number of times a candidate is repeated for each candidate and store it is a dictionary

#Percentage of votes each candidate won
#Take the values for each candidate and divide it by the total count and then multiply it by 100


#The winner of the election based on popular vote
#Identify the candidate with the maximum percentage of votes
'''
#Importing modules
import csv
import os

#Reference to file to read
file_to_read=os.path.join("Resources","election_results.csv")

#Opening and reading the file
with open(file_to_read,'r') as election_data:
    #Analysis of the file
    file_reader=csv.reader(election_data)
    header=next(file_reader)
    print(header)
    '''
    for row in file_reader:
        print(row)
    '''

#File to save the output to
file_to_save=os.path.join("analysis","election_analysis.txt")

#Opening file to write 
with open(file_to_save,'w') as txt_file:
    txt_file.write("Counties in the election\n---------------------------\n")
    txt_file.write ("Arapahoe\nDenver\nJefferson")
