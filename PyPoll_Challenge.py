# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources3", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
# counties = [] unecessary will use keys of county votes
county_votes = {}
county_list = []
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_name = ""
largest_county_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]       
        # If the candidate does not match any existing candidate add it to 
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
     
   # # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
#    #print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"                                                                                             
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
#     # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

#         # 6b: Retrieve the county vote count.
#         # 6c: Calculate the percentage of votes for the count
#          # 6d: Print the county results to the terminal.
#          # 6e: Save the county votes to a text file.
# 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > largest_county_turnout):
            largest_county_turnout = votes
            largest_county_name = county_name
            #print(f'Largest = {largest_county_turnout}')
            #print(f'Prior Largest = {votes}')
            #print(f'largest_county_name = {largest_county_name}')
            #print(f'prior largest = {county_name}')
    largest_county_summary = (f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(f"winning county:{largest_county_name}")
#     # 7: Print the county with the largest turnout to the terminal.
#     # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_name)
#     # Save the final candidate vote count to the text file.
#     for candidate_name in candidate_votes:
#         # Retrieve vote count and percentage
#     # 
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
#         # Determine winning vote count, winning percentage, and candidate.
        if (winning_count < votes) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
#     # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
#     # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
