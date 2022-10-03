# import dependencies
import os
import csv

# file path to open csv
poll_data = os.path.join( "Resources", "election_data.csv")

# Store variables
total_votes = 0
cand_votes = 0

# list to store candidates names
unique_candidates = []
list_votes = []
winning_votes = []

# dictionary to store candidates and votes
cand_and_votes = {}

# open and read CSV file
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # skip header
    next(csvreader)

    # initialize loop for every row of data
    for rows in csvreader:
        
        #count every vote
        total_votes += 1
        #store the candidate row as variable
        names = rows[2]

        # if name does not appear in 3rd column,
        if names not in unique_candidates:
            #add name to list unique candidates
            unique_candidates.append(names)
            # add votes into dictionary and 1 vote for first time they appear
            cand_and_votes[names] = {'votes':1}
        else:
            # add a vote to every time their name appears
            cand_and_votes[names]['votes'] += 1
        
        # loop through names in the dictionary and find percent to total votes
        for names in cand_and_votes:
            cand_and_votes[names]['percent_votes'] = round((cand_and_votes[names]['votes']/total_votes)*100,3)

# write to text file
with open('analysis/PyPoll Analysis.txt',"w") as txt_file:

    # variable the header and vote count
    header = (F"Election Results\n ------------\nTotal Votes: {total_votes}\n------------\n")   
    # write the header into text file
    txt_file.write(header)
    print(header)

    # loop through and find the total votes by candidates
    for x in unique_candidates:

        # winning_votes.append()
        election_results = (f"{x} {cand_and_votes.get(x)['percent_votes']}% ({cand_and_votes.get(x)['votes']}) \n")
        print(election_results)

        # append votes into list
        votes = cand_and_votes.get(x)['votes']
        list_votes.append(votes)

        # find max of votes
        winning_votes = max(list_votes)

        # find index of max votes
        index_winning_vote = list_votes.index(winning_votes)

        #write the election results in text
        txt_file.write(election_results)

    # with max vote index, find candidate
    winner = unique_candidates[index_winning_vote]
    winner_text =(f"----------\nWinner: {winner}\n---------\n")

    #write the winner into text
    txt_file.write(winner_text)
    print(winner_text)

