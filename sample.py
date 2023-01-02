def vote_winner(lst):
    candidates = set(lst)  # Converting a list into set to have all candidate names
    for i in candidates:  # Iterating over candidate
        count = 0  # To count the vote of a candidate
        for j in lst:  # Iterating over votes
            if i == j:  # If vote is same as candidate
                count = count + 1  # Update count
            if count > len(lst) / 2:  # If count is greater than 50% of votes, return winner
                return i
    return None  # If no candidate has more than 50% of votes, return None


dummy_lst = ['John', 'Mary', 'John']  # Dummy data
print("Winner is :", vote_winner(dummy_lst))  # Calling above function
