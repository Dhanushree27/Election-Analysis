
# Election Analysis

## Project Overview
A Colorado Board of Election employee has given the following tasks to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the percentage of votes from each county
4. Determine the county with the highest turnout
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Resources
**Data Source:** election_results.csv

**Software:** Python 3.9.5, Visual Studio Code 1.61.1

## Summary
The analysis of the election results show that:
- There were a total of 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson county received 10.5% of votes and a total number of 38,855 votes
  - Denver county received 82.8% of votes and a total number of 306,055 votes
  - Arapahoe county received 6.7% of votes and a total number of 24,801 votes
- **Denver** county had the larger turnout with 306,055 votes
- The candidate results were:
  - Charles Casper Stockham received 23.0% of votes and a total number of 85,213 votes
  - Diana DeGette received 73.8% of the votes and total number of 272,892 votes
  - Raymon Anthony Doane received 3.1% of the votes and total number of 11,606 votes
- The winner of the election was:
  - Candidate **Diana DeGette** received **73.8%** of the votes and total number of **272,892** votes

## Challenge Overview
The challenge required two analyses in addition to the analyses carried out initially:
1. Calculate the percentage of votes from each county
2. Determine the county with the highest turnout

### Percentage of votes for each county
The calculation of percentage for each county required iterating through each county similar to the iteration for each candidate. Steps involved:
- Determine the unique list of counties
- Determine the votes for each county
- Iterate through each county and divide the individual vote by total votes 

```
 for county_name in county_list:

        # Retrieving the county vote count.
        county_vote=county_votes[county_name]
        # Calculating the percentage of votes for the county.
        county_percentage=float(county_vote/total_votes) *100

        # Printing the county results to the terminal.
        print(f"{county_name}: {county_percentage:.1f}% ({county_vote:,})")
        # Saving the county votes to a text file.
        txt_file.write(f"{county_name}: {county_percentage:.1f}% ({county_vote:,})\n")
```
The data was directly written into a file instead of being stored 

### County with the highest turnout
The calculation involved looping through each county to check whether its turnout was greater than the previous counties. If so, then it replaced the value of the previous county.
```
for county_name in county_list:
        # If statement to determine the winning county and get its vote count.
        if county_vote>winning_turnout:
            winning_turnout = county_vote
            winning_county = county_name
```
## Challenge Summary
Based on the output from the script, it can be seen that the code is a good way to summarize election results. It takes into account, both the county and the candidate name and provides a brief summary. This script can be re-used for any election by modifying a few parameters. The reference file can be modified to reflect the kind of election data being analysed. This code can also be adapted for a more detailed analysis and also for different kinds of elections with a few modifications:

**Example 1**: Currently this code has been structured for county level elections. This can even be configured for Presidential level elections. It can be done at the high level by using the party name as data instead of the candidate name and the state name instead of the county name. 

Additionally, more columns can be added to the data, and additional sections to the code. For example, we can collect data on state, county and party. The current code already contains information on county, and party(candidate name). It can be updated to include a similar section for state and that information can be written to the document as well

**Example 2**: The code can expanded to provide a more detailed summary by listing how each candidate performed in each county. This can be achieved by creating a list of dictionaries with the county name, candidate name and the votes in each county, for each candidate. This can then be used to create summaries as required

