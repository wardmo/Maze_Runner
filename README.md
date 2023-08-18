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

### I want to generate a png during each step of the generation process to animate how the algorithm works
