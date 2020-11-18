# Djıkstra shortest path with open street maps data
### About:
A shortest path algorithm in djikstra (or something like it) implemented with open streets maps data
It's written in python 3.8 using only the std library.

### Design process: 
Initially I tried to do this with a very greedy algorithm 
(I _always_ took the shortest distanced path)
but that didn't work so well... :D 

I approached the problem like the above because I thought that 
dijkstra was going to give me some stackoverflow errors with this dataset,
and while trying to do A*, I had some problems determining the estimate functions.

But after completing the extremely greedy algo, I realised that it was not the optimal soln. 
(It returned the distance way larger than it should + it took too long), I debugged it for a while, 
then decided to give dijkstra a shot, and if needed some; optimisation.

Well, I'm writing this because dijkstra works :tada: with the example dataset.

#### Assumptions:
- I don't know if this code would work with a larger dataset. As far as I'm aware is that it should,
 so I assumed the computer executing this would have enough RAM.
- I assumed that there won't be any junk data after the edges, but still included the slicing for it in the end. 

### Dependencies: 
python 3.8
shell

### How to run:
- With python:
`python main.py <start_vertex> <end_vertex>`
