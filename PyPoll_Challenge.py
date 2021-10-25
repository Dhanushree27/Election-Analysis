# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Importing modules
import csv
import os

# Defining file to read data from 
file_to_load = os.path.join("Resources","election_results.csv")
# Defining file to save output to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initializing list and dictionary to store candidate information
candidate_options = []
candidate_votes = {}
# Initializing list and dictionary to store candidate and county information
county_list=[]
county_votes={}

# Initializing variables to track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Initializing variables to track the largest county and county voter turnout.
winning_county=""
winning_turnout=0

# Reading the csv and converting it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Reading the header (Skips the header)
    header = next(reader)

    # Reading each row in the CSV file.
    for row in reader:

        # Adding to the total vote count by counting rows
        total_votes = total_votes + 1
        # Getting the candidate name from each row.
        candidate_name = row[2]
        # Extracting the county name from each row.
        county_name=row[1]

        # If the candidate does not match any existing candidate adding it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Adding the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Beginning to track that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Adding a vote to each candidate's count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county adding it to
        # the county list.
        if county_name not in county_list:

            # Adding the county name to the county list.
            county_list.append(county_name)
            # Beginning to track that county's vote count.
            county_votes[county_name]=0

        # Adding a vote to each county's vote count.
        county_votes[county_name]+=1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Printing the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Saving the final vote count to a text file
    txt_file.write(election_results)

    # Calculating votes for each county
    for county_name in county_list:

        # Retrieving the county vote count.
        county_vote=county_votes[county_name]
        # Calculating the percentage of votes for the county.
        county_percentage=float(county_vote/total_votes) *100

        # Printing the county results to the terminal.
        print(f"{county_name}: {county_percentage:.1f}% ({county_vote:,})")
        # Saving the county votes to a text file.
        txt_file.write(f"{county_name}: {county_percentage:.1f}% ({county_vote:,})\n")

        # If statement to determine the winning county and get its vote count.
        if county_vote>winning_turnout:
            winning_turnout = county_vote
            winning_county = county_name
                 
    # Printing the county with the largest turnout to the terminal.
    winning_county_summary=(
        f"\n-------------------------\n"
        f"Largest county turnout: {winning_county} ({winning_turnout:,})\n"
        f"-------------------------\n")  
    print(winning_county_summary)
    # Saving the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)
    
    # Saving the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieving vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Printing each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Saving the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determining winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Printing the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Saving the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
