from Protocols import Solver, MazeContract, Animator
from Maze_Types import Maze_Types as MAZE
from Animator import NullAnimator
from collections import deque


class Solve(Solver):
    @staticmethod
    def create_adjacency_list(maze:MazeContract) -> MAZE.AdjacencyList:
        adj:MAZE.AdjacencyList = {}
        edge:MAZE.Edge
        for edge in maze.paths:
            n1:MAZE.NodeId
            n2:MAZE.NodeId
            n1,n2 = edge
            if n1 in adj:
                adj[n1].add(n2)
            else:
                adj[n1] = {n2}
            if n2 in adj:
                adj[n2].add(n1)
            else:
                adj[n2] = {n1}
        return adj
    
    
    @staticmethod
    def SolveDFS(maze:MazeContract, animator:Animator=NullAnimator()) -> set[MAZE.NodeId]:
        start:MAZE.NodeId = (0,0)
        end:MAZE.NodeId = (maze.height-1, maze.width-1)
        frontier:list[MAZE.NodeId] = [start]
        visited:set[MAZE.NodeId] = set()
        adjacency_list:MAZE.AdjacencyList = Solve.create_adjacency_list(maze)
        solution:dict[MAZE.NodeId,MAZE.NodeId] = {}
        current:MAZE.NodeId = start
        while frontier:
            current = frontier.pop()
            if current == end:
                break
            visited.add(current)
            animator.save_frame(maze, solution_nodes=set(visited))
            next_node:MAZE.NodeId
            for next_node in adjacency_list[current]:
                if next_node in visited:
                    continue
                else:
                    frontier.append(next_node)
                    solution[frontier[-1]] = current

        path:set[MAZE.NodeId] = set()
        path.add(start)
        while end != start:
            path.add(end)
            end = solution[end]
        for _ in range(15):
            animator.save_frame(maze, solution_nodes=path)
        return path
    
    @staticmethod
    def SolveBFS(maze:MazeContract, animator:Animator=NullAnimator()) -> set[MAZE.NodeId]:
        visited:list[MAZE.NodeId] = list()
        adjacency_list:MAZE.AdjacencyList = Solve.create_adjacency_list(maze)
        _deque:deque[list[MAZE.NodeId]] = deque()
        start:MAZE.NodeId = (0,0)
        end:MAZE.NodeId = (maze.height-1,maze.width-1)
        _deque.append([start])
        while _deque:
            path:list[MAZE.NodeId] = _deque.pop()
            node:MAZE.NodeId = path[-1]
            if node not in visited:
                neighbors:list[MAZE.NodeId] = adjacency_list[node]
                for neighbor in neighbors:
                    new_path:list[MAZE.NodeId] = list(path)
                    new_path.append(neighbor)
                    _deque.append(new_path)

                    if neighbor == end:
                        retval = set(new_path)
                        for _ in range(15):
                            animator.save_frame(maze, solution_nodes=retval)
                        return retval
                visited.append(node)
                animator.save_frame(maze, solution_nodes=set(visited))