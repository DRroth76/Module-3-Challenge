# imports modules needed
import csv

# sets file path
election_csv = r'C:\Users\David Roth\data_analysis_bootcamp\module3\cloned_module3challenge_files\Module-3-Challenge\PyPoll\Resources\election_data.csv'
election_txt = r'C:\Users\David Roth\data_analysis_bootcamp\module3\cloned_module3challenge_files\Module-3-Challenge\PyPoll\analysis\analysis_results.txt'

# establish lists
ballot_id = []
county = []
candidate = []

# to open the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    data = list(csvreader)

# establishing variables
    total_votes = 0
    stockham_vote_count = 0
    stockham_percentage = 0
    degette_vote_count = 0
    degette_percentage = 0
    doane_vote_count = 0
    doane_percentage = 0
    winner = ''

# for loop to pull data
    for row in data:
        ballot_num = str(row[0])
        candidate_name = str(row[2])

        ballot_id.append(ballot_num)
        candidate.append(candidate_name)

# if statements to count votes
        if candidate_name == "Charles Casper Stockham":
            stockham_vote_count += 1
        elif candidate_name == "Diana DeGette":
            degette_vote_count += 1
        elif candidate_name == "Raymon Anthony Doane":
            doane_vote_count += 1
    
            total_votes = stockham_vote_count + degette_vote_count + doane_vote_count
            stockham_percentage = round((stockham_vote_count / total_votes) * 100, 3)
            degette_percentage = round((degette_vote_count / total_votes) * 100, 3)
            doane_percentage = round((doane_vote_count / total_votes) * 100, 3)

    
# if statements to find the winner
    if stockham_vote_count > degette_vote_count and doane_vote_count:
        winner = "Charles Casper Stockham"
    elif degette_vote_count > doane_vote_count:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
# print results and winner
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {stockham_percentage}% ({stockham_vote_count})")
print(f"Diana DeGette: {degette_percentage}% ({degette_vote_count})")
print(f"Raymon Anthony Doane: {doane_percentage}% ({doane_vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# to print to text file
with open(election_txt, "w") as text_file:
    output = (
       "Election Results\n"
       "-------------------------\n"
       f"Total Votes: {total_votes}\n"
       "-------------------------\n"
       f"Charles Casper Stockham: {stockham_percentage}% ({stockham_vote_count})\n"
       f"Diana DeGette: {degette_percentage}% ({degette_vote_count})\n"
       f"Raymon Anthony Doane: {doane_percentage}% ({doane_vote_count})\n"
       "-------------------------\n"
       f"Winner: {winner}\n"
       "-------------------------\n"
    )
    text_file.write(output)