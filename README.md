# Maze_Runner

## Usage:

## Print to console
```python
maze = Maze.GenerateFromDFS(14,40)
solution = Solve.SolveBFS(maze)
print(MazeVisualizer(maze, solution_nodes=solution))
```
<img src="https://i.imgur.com/OZN2Iq0.png" alt="your picture is broken" width="500"/>

## Save as png
```python
maze = Maze.GenerateFromPrims(250,250)
solution = Solve.SolveDFS(maze)
rep = MazeVisualizer(maze, solution_nodes=solution)
rep.save_img('prims.png')
```
![your picture is broken](https://i.imgur.com/qGwNfHM.png)

## Animate Maze Generation
```python
my_animator = ConcreteAnimator()
Maze.GenerateFromWilsons(40,40,animator=my_animator)
animator.animate('wilsons.gif')
```
<img src="https://i.imgur.com/OyGeWT4.gif" alt="your picture is broken" width="500"/>

## Animate Maze Generation and Solve
```python
animator = ConcreteAnimator()
krus = Maze.GenerateFromKruskal(40,40,animator=animator)
Solve.SolveDFS(krus, animator=animator)
animator.animate('krus_full_generate_solve.gif')
```
<img src="https://i.imgur.com/gKloc7r.gif" alt="your picture is broken" width="500"/>


## Next steps

### Add a timer to see which algorithms generate mazes the fastest, which algorithms solve the fastest
  
Maze Generation Algorithms from here:  
https://en.wikipedia.org/wiki/Maze_generation_algorithm

Origin Shift Generation Algorithm from here:
https://www.youtube.com/watch?v=zbXKcDVV4G0&list=LL&index=2&t=72s
