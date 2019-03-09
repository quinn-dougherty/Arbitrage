# Chess Tournament and Betting with fake money

### View `notes.ipynb` to see everything in action! 

# COUNTDOWN TO MVP
- sqlize-- make sure it works
- flaskize-- show a simple dashboard of each df in the `Book` object
- implement **endgame** payout

## *Stretch*
- --count the top `N` finishers, where `N` equals 1/5 the number of people who signed up. So if 10 people sign up, then payouts take into account first and second place. This will be fairly easy--- if you bet against a person who finishes second, you only get 80% of the payout, etc. 
- *ENDGAME* implement estimated endgame from any point, sort of like a null hyp montecarlo 
- write reports translating the probablistic interpretation of odds
- *ENDGAME*: show calibration plot and Brier score for endgame, both projected and actual

### NOTES: 

- Double Round Robin: length 2 permutations of competitors represents the set of games. 

- each bettor gets λ100, and the house will initialize at (null hypothesis) 1:1 odds on each player. I'll represent the house as a forecaster/bettor, just giving it more starter cash (like λ1000) and generating the null hyp bets

- Bettors can look at the current accumulated score for each player, and submit bets basically whenever. 
 
- competitors will have to be 100% signed up in advance. We cannot admit new competitors once the tournament begins 

- Bettors can sign up on a rolling basis. they get initialized with λ100
- - I'm also at this point planning every `mark_winner` actually replenishes a dollar to every bettor, to help keep things interesting.  


