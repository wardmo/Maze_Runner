# Maze_Runner

## Usage:
```python
maze = Maze.GenerateFromDFS(14,40)
solution = Solve.SolveBFS(maze)
print(MazeVisualizer(maze, solution_nodes=solution))
```
```python
maze = Maze.GenerateFromPrims(250,250)
solution = Solve.SolveDFS(maze)
rep = MazeVisualizer(maze, solution_nodes=solution)
rep.save_img('prims.png')
```
## Print to console
![your picture is broken](https://i.imgur.com/OZN2Iq0.png)

## Save as png
![your picture is broken](https://i.imgur.com/qGwNfHM.png)


## Next steps

### I want to generate a png during each step of the generation process to animate how the algorithm works


### Add a timer to see which algorithms generate mazes the fastest, which algorithms solve the fastest
  
Maze Generation Algorithms from here:  
https://en.wikipedia.org/wiki/Maze_generation_algorithm
