# codeforce_478B-random-team
n participants of the competition were split into m teams in some manner so that each team has at least one participant. 
After the competition each pair of participants from the same team became friends.  
Your task is to write a program that will find the minimum and the maximum number of pairs of friends that could have formed by the end of the competition.

INPUT::
The only line of input contains two integers n and m, separated by a single space (1 ≤ m ≤ n ≤ 109) — the number of participants and the number of teams respectively.

OUTPUT::
The only line of the output should contain two integers kmin and kmax — the minimum possible number of pairs of friends and the maximum possible number of pairs of friends respectively.

example 1:

input

6 3

output

3 6

(minimum number of newly formed friendships can be achieved if participants were split on teams consisting of 2 people, maximum number can be achieved if participants were split on teams of 1, 1 and 4 people.)

Example 2:

input

5 1

output

10 10

(all the participants get into one team, so there will be exactly ten pairs of friends.)
