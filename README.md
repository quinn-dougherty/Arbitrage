# Chess Tournament and Betting with fake money

view `notes.ipynb` to see boards in action. 
they're just representing the games and the players currently. 

the book hasn't begun to be implemented, i have some notes about it in `entities.py`. 

NOTES: 

Double Round Robin: length 2 permutations of competitors represents the set of games. 

- ~~competition will be `P(n,2)` games long, if we have n players competing.~~ 
### this is implemented, but i need to check with Rudy to make sure i interpreted double-round-robin correctly

~~scoring is this: ~~
- ~~when a player wins, they are awarded 1 point~~
- ~~when a player loses, they are awarded 0 points~~ 
- ~~in a draw, they are awarded 0.5 points.~~
### implemented, we can adjust the values in global vars in boards.py

## competitors will have to be 100% signed up in advance. I don't think we can admit new competitors once the tournament begins? 

## We should be able to let bettors sign up on a rolling basis. they get initialized with λ100



Betters can look at the current accumulated score for each player, and submit bets basically whenever. 

- QUESTION (Rudy?)--- do we have to _remember_ who exactly a player won/lost/drawed against, or can we just delete that information and only keep track of it in the form of the accumulated score. 

what they're betting _on_ is the outcome at the very end--- the final score. 

each bettor gets λ100, and the house will initialize at (null hypothesis) 1:1 odds on each player. I'll represent the house as a forecaster/bettor, just giving it more starter cash (like λ1000) and generating the null hyp bets

- Should we have a mechanism for partial/depleted payouts if you bet on someone who got 2nd, 3rd, 5th place?? I don't know the details. I could do it as a basic discount factor but i think that might require unlimited house pot (rather than an arbitrary but fixed pot of like λ1000). 



