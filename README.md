# Maze_Runner

Maze Generation Algorithms from here:  
https://en.wikipedia.org/wiki/Maze_generation_algorithm


usage:
```python
maze = DFS_Generation(14,40)  
print(Maze_Rep(maze, solution_nodes=BFS(maze).solve()))
```
```python
maze = Prims_Generation(250,250)
rep = Maze_Rep(maze, solution_nodes=BFS(maze).solve())
rep.save_img('prims.png')
```
## Print to console
![your picture is broken](https://i.imgur.com/OZN2Iq0.png)

## Save as png
![your picture is broken](https://i.imgur.com/qGwNfHM.png)


## Next steps

### I want to have a better visualization solution, printing to the console has certain limits
Got this taken care of, but now realizing that generating large mazes with DFS_Generation causes python to break with a RecursionError: maximum recursion depth exceeded while calling a Python object.  
should refactor DFS_Generation with an iterative implementation instead of recursive
