# Author: Anthony Lozito
# Colorado Election Project

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("C:\\", "Users", "ajloz", "Election_Analysis", "Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("C:\\", "Users", "ajloz", "Election_Analysis", "Election Analysis", "election_analysis.txt")   

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: Initialize a county list and county votes dictionary
county_names = []
voting_counties = {}

# Initialize the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Initialize the largest county with their voter turnout
largest_county = ""
votes_by_county = 0

# Read and copy candidates and counties from the csv file to create dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Retrieve the candidate name from each row
        candidate_name = row[2]
        
        # 3: Retrieve the county name from rows
        county_name = row[1]
        
        # Append the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Track the vote count by candidate
            candidate_votes[candidate_name] = 0

        # Add vote to a candidate's vote count
        candidate_votes[candidate_name] += 1

        # 4a: Check if the county is in the original county list from Step 1
        if county_name not in county_names:

            # 4b: Append new county names to the original county list from Step 1
            county_names.append(county_name)

            # 4c: Track the vote count by county
            voting_counties[county_name] = 0

        # 5: Add vote a county's vote count
        voting_counties[county_name] += 1


# Save the results as a text file
with open(file_to_save, "w") as txt_file:

    # Print the overall total vote count and vote count by county
  
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")

    # Save vote count to the text file
    txt_file.write(election_results)

    # 6a: Create a for loop to retrieve the county from the county dictionary
    for county in voting_counties:

        # 6b: Intialize a variable to hold the county's votes as they are retrieved the county dictionary
        voting_county = voting_counties[county]

        # 6c: Calculate each county's votes as a percentage of all votes received
        voter_turnout = int(voting_county) / int(total_votes) * 100
        county_results = (f"{county}: {voter_turnout:.1f}% ({voting_county:,})\n"
        )

         # 6d: Print the vote count by county
        print(county_results, end="")

         # 6e: Save the vote count by county to the text file
        txt_file.write(county_results)

         # 6f: Create an if statement that determines the largest county and provides that county's vote count
        if (voting_county > votes_by_county):
            votes_by_county = voting_county
            largest_county = county
    
    # 7: Print the county with the largest voter turnout to the terminal
    largest_county = (
        f"-------------------------\n"
        f"Largest County: {largest_county}\n"
        f"-------------------------\n"
    )
    print(largest_county)

    # 8: Save the county with the largest voter turnout to the terminal
    txt_file.write(largest_county)

    # Save the total vote count by candidate to the text file
    for candidate in candidate_votes:

        # Retrieve each candidate's vote count and percentage of the vote 
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )

        # Print each candidate's vote count and percentage to the terminal

        print(candidate_results)

        #  Save the results by candidate to the text file
        txt_file.write(candidate_results)

        # Determine the winning candidate and show their results by vote count and percentage of the total votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the results of the winning candidate to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        )
    
    print(winning_candidate_summary)
    
    # Save the winning candidates results to the text file
    txt_file.write(winning_candidate_summary)