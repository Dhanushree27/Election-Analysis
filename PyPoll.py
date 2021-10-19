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
#File to save the output to
file_to_save=os.path.join("analysis","election_analysis.txt")

#Initializing variables
total_votes=0
winning_candidate=""
winning_votes=0
winning_percentage=0.0
#Initializing list for candidate names
candidate_options=[]
#Initializing dictionary for candidate votes
candidate_votes={}

#Opening and reading the file
with open(file_to_read,'r') as election_data:
    file_reader=csv.reader(election_data)

    #Read, skip the header row. Next automatically moves to the next item on list, so for starts from the second row
    header=next(file_reader)
        
    #Loop to read each row in file
    for row in file_reader:
        #Incrementing value as row count increases
        total_votes+=1
        #Identifying list of candidates by adding candidate if name is not already present
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            #List of candidates
            candidate_options.append(candidate_name)
            #Initializing vote count for each candidate
            candidate_votes[candidate_name]=0
        #Tallying votes per candidate
        candidate_votes[candidate_name] +=1

    #Opening file to write results
    with open(file_to_save,'w') as txt_file:
        election_results=(
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        #Writing election results
        txt_file.write(election_results)
        print(election_results,end="")  

        #Calculating the percentage of votes for each candidate
        for candidate in candidate_options:
            votes=candidate_votes[candidate]
            Percentage_votes=float(votes/total_votes)*100

            #Writing the results for each candidate
            candidate_results=(f"{candidate} : {Percentage_votes:.1f}% ({votes:,})\n")
            txt_file.write(candidate_results)
            print(candidate_results)

            #Determining the winning votes, percentage by replacing as required
            if votes>winning_votes and Percentage_votes>winning_percentage:
                winning_votes=votes
                winning_percentage=Percentage_votes
                winning_candidate=candidate

        #Writing summary results
        win_summary=(
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_votes:,}\n"
            f"Winning percentage: {winning_percentage:.1f}\n"
            f"-------------------------\n")
        print(win_summary)
        txt_file.write(win_summary)
        

    
