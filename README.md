# Maze_Runner

Maze Generation Algorithms from here:  
https://en.wikipedia.org/wiki/Maze_generation_algorithm


usage:  
maze = DFS_Generation(14,40)  
BFS(maze).solve()  
print(Maze_Rep(maze))  

![your picture is broken](https://i.imgur.com/OZN2Iq0.png)


## Next steps

I want to have a better visualization solution, printing to the console has certain limits

I want to refactor the solvers and mazes to follow the Protocols a little more closely.  
I think the solution_nodes should belong to the Solver classes instead of the maze classes  
I would rather have the usage be something like:  
maze = DFS_Generation(height, width)  
rep = Maze_Rep(maze)  
print(rep)  
solution = BFS(maze).solve()  
print(Maze_Rep(maze, solution=solution))  

enabling printing a maze before and after solving without having to create a whole new Maze_Rep object
