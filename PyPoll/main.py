
# coding: utf-8

# In[2]:


import csv


# In[7]:

def count_votes():
    with open('PyPollData.csv') as file:
        poll_data = csv.reader(file, delimiter=",")
        next(poll_data)
        total_votes = 0
        candidates = {}
        for row in poll_data:
            candidate = row[2]
            if candidate not in candidates:
                candidates[candidate] = 1
            else:
                candidates[candidate] += 1
            total_votes += 1
        vote_candidates = []
        for k, v in candidates.items():
            vote_candidates.append(f'{k}: {round((v/total_votes)*100, 2)}% ({v})')
        candidate_list = "\n".join(vote_candidates)
        winner = max(candidates.keys(), key=(lambda k: candidates[k]))
        return \
        f'''Election Results
        ---------------------
        Total Votes: {total_votes}
        ---------------------
        {candidate_list}
        ---------------------
        Winner: {winner}
        ---------------------
        '''
output = count_votes()
print(output)
with open("pypoll.txt", "w") as file:
    file.write(output)
