# Chess Tournament and Betting with fake money

NOTES: 

Double Round Robin: length 2 permutations of competitors represents the set of games. 

- competition will be `P(n,2)` games long, if we have n players competing. 

scoring is this: 
- when a player wins, they are awarded 1 point
- when a player loses, they are awarded 0 points 
- in a draw, they are awarded 0.5 points.

Betters can look at the current accu scores and the history of wins/losses/draws for each player, and submit bets basically whenever. 

what they're betting _on_ is the outcome at the very end--- the final score. 

Perhaps there should be some system for 

each better gets $100 fake dollars, and the house will initialize at (null hypothesis) 1:1 odds on each player. 
