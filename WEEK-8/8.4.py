Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.

Examples: 

Input :  votes[] = {"john", "johnny", "jackie",

                    "johnny", "john", "jackie",

                    "jamie", "jamie", "john",

                    "johnny", "jamie", "johnny",

                    "john"};

Output : John

We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem

 

Sample Input:

10

John

John

Johny

Jamie

Jamie

Johny

Jack

Johny

Johny

Jackie

 

Sample Output:

Johny

Code:
def find_winner(votes):
    vote_count = {}
    for candidate in votes:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    max_votes = max(vote_count.values())
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
    return min(winners)

n = int(input().strip())
votes = [input().strip() for _ in range(n)]
print(find_winner(votes))
