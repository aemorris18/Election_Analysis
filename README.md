# Election_Analysis
python
Election Audit Results

At the request of the election commission the analysis includes the voter turnout for each country, the percentage of votes from each county out the total count and the county with the highest turnout.

The election audit result are as follows:
•	Total Votes: 369,711
•	Counts per county:
      		       Jefferson 38,855 (10.5%)
		       Denver 306.055 (82.8%)
 		       Arapahoe 24, 801 (6.7%)
Code: 
for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

•	County with largest votes:
        Denver
          Code:
if (votes > largest_county_turnout):
            largest_county_turnout = votes
            largest_county_name = county_name

•	Votes Per Candidate:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
      Code
for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

•	Winning Candidate:
          Diana DeGette
          272,892 Total Votes to Candidate
          73.8% of Total Votes
Summary:
There were three counties in this congressional district with Denver county contributing the largest number of votes in the election with 82.8%. Diana De Gette is the winner with 73.8% of the votes. With modifications this script can be used on local county elections and national elections. Additionally, we can add scripts to determine total votes by party and winning votes by party.
![image](https://user-images.githubusercontent.com/106499082/177664093-d8beafd5-86e5-4323-b8b5-a7e52225f4d2.png)
