# Maze_Runner

Maze Generation Algorithms from here:  
https://en.wikipedia.org/wiki/Maze_generation_algorithm


usage:
```python
maze = DFS_Generation(14,40)  
print(Maze_Rep(maze, solution_nodes=BFS_Solver(maze).solve()))
```

![your picture is broken](https://i.imgur.com/OZN2Iq0.png)


## Next steps

I want to have a better visualization solution, printing to the console has certain limits

I want to refactor the solvers and mazes to follow the Protocols a little more closely.  

enabling printing a maze before and after solving without having to create a whole new Maze_Rep object
