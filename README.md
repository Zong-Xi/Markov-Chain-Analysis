# Queueing Theory: Analysis the Markov-Chain on Traffic Congestion

## Problem Description
Traffic congestion problem cause slower speed, longer trip time, and vehicular queueing. Traffic congestion problem usually happen at the interaction when traffic demand increase. We can describe the queueing problem as a Markov process, and find out the transition matrix of the Markov chain 

## Parameter
* p: the probability of a car coming at the time step
* q: the probability of no car coming at the time step 
* k: the length of queue at the steady-state 

## The Project contain:
* Mathematical derivation of transition matrix (green light and red light)
* Mathematical derivation of probability distribution at steady-state
* Result of simulation

## Run the code
* `python code.py --p --k`
* p: the probability of a car coming at the time step
* k: the length of queue at the steady-state 
* ex: `python code.py --0.45 --5`
