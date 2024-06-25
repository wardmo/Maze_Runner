from Protocols import MazeContract, Animator
from Animator import NullAnimator
from Maze_Types import Maze_Types as MAZE
from random import shuffle, choice


class Maze(MazeContract):
    def __init__(self,paths:set[MAZE.Edge], height:int, width:int, nodes=None) -> None:
        self.paths = paths
        self.nodes = set((j,i) for i in range(width) for j in range(height)) if nodes is None else nodes
        self.width = width
        self.height = height
        pass

    @staticmethod
    def GenerateFromKruskal(height_nodes:int, width_nodes:int, animator:Animator=NullAnimator()) -> MazeContract:

        nodes:set[MAZE.NodeId] = set()
        maze_nodes:set[MAZE.NodeId] = set()
        edges:set[MAZE.Edge] = set()
        for j in range(height_nodes):
            for i in range(width_nodes):
                current_node = (j,i)
                nodes.add(current_node)
                if i < width_nodes - 1:
                    edges.add((current_node, (j,i+1)))
                if j < height_nodes - 1:
                    edges.add((current_node, (j+1, i)))
                
        clusters:dict[MAZE.NodeId,MAZE.NodeId] = {n:n for n in nodes}
        ranks:dict[MAZE.NodeId, int] = {n:0 for n in nodes}
        solution: set[MAZE.NodeId] = set()
        edgelist: list[MAZE.NodeId] = list(edges)

        def find(n:MAZE.NodeId):
            if clusters[n] != n:
                clusters[n] = find(clusters[n])
            return clusters[n]
            pass

        def union(n1:MAZE.NodeId, n2:MAZE.NodeId):
            x,y = find(n1),find(n2)
            if ranks[x] == ranks[y]:
                clusters[y] = x
            else:
                clusters[x] = y
            if ranks[x] == ranks[y]:
                ranks[y] += 1
            pass


        shuffle(edgelist)


        n1: MAZE.NodeId
        n2: MAZE.NodeId
        for n1, n2 in edgelist:
            if find(n1) != find(n2):
                solution.add((n1,n2))
                maze_nodes.add(n1)
                maze_nodes.add(n2)
                animator.save_frame(Maze(set(solution), height_nodes,width_nodes, nodes=set(maze_nodes)))
                union(n1,n2)

        return Maze(solution, height_nodes, width_nodes)
    
    @staticmethod
    def GenerateFromPrims(height_nodes:int, width_nodes:int, animator:Animator=NullAnimator()) -> MazeContract:

        def get_edges(node:MAZE.NodeId) -> list[MAZE.Edge]:
            j,i = node
            edges:list[MAZE.Edge] = []
            if i < width_nodes - 1:
                edges.append((node, (j,i+1)))
            if i > 0:
                edges.append((node, (j,i-1)))
            if j < height_nodes - 1:
                edges.append((node, (j+1,i)))
            if j > 0:
                edges.append((node, (j-1,i)))
            return edges
            pass

        nodes:set[MAZE.NodeId] = set()
        edges:set[MAZE.Edge] = set()
        for j in range(height_nodes):
            for i in range(width_nodes):
                current_node = (j,i)
                nodes.add(current_node)
                if i < width_nodes - 1:
                    edges.add((current_node, (j,i+1)))
                if j < height_nodes - 1:
                    edges.add((current_node, (j+1,i)))
        first_node:MAZE.NodeId = choice(tuple(nodes))
        visited:set[MAZE.NodeId] = {first_node}
        solution:set[MAZE.Edge] = set()
        lst:list[MAZE.Edge] = get_edges(first_node)
        animator.save_frame(Maze(set(solution), height_nodes, width_nodes, nodes=set(visited)))
        while lst:
            n1:MAZE.NodeId
            n2:MAZE.NodeId
            n1,n2 = lst.pop(choice(range(len(lst))))
            if (n1 in visited and n2 not in visited) or (n2 in visited and n1 not in visited):
                solution.add((n1,n2))
                if n1 not in visited:
                    visited.add(n1)
                    lst.extend(get_edges(n1))
                if n2 not in visited:
                    visited.add(n2)
                    lst.extend(get_edges(n2))
                animator.save_frame(Maze(set(solution), height_nodes, width_nodes, nodes=set(visited)))
        return Maze(solution, height_nodes, width_nodes)
    
    @staticmethod
    def GenerateFromDFS(height_nodes:int, width_nodes:int, animator:Animator=NullAnimator()) -> MazeContract:


        nodes:set[MAZE.NodeId] = set((j,i) for i in range(width_nodes) for j in range(height_nodes))
        visited:set[MAZE.NodeId] = set()

        def unvisited_neighbor_nodes(node:MAZE.NodeId) -> list[MAZE.NodeId]:
            j,i = node
            unvisited_nodes:MAZE.NodeId = set()
            next:MAZE.NodeId
            if i < width_nodes - 1:
                next = (j, i+1)
                if next not in visited:
                    unvisited_nodes.add((j,i+1))
            if i > 0:
                next = (j, i-1)
                if next not in visited:
                    unvisited_nodes.add((j,i-1))
            if j < height_nodes - 1:
                next = (j+1, i)
                if next not in visited:
                    unvisited_nodes.add((j+1, i))
            if j > 0:
                next = (j-1,i)
                if next not in visited:
                    unvisited_nodes.add((j-1, i))
            return list(unvisited_nodes)

        paths:set[MAZE.Edge] = set()
        first:MAZE.NodeId = choice(list(nodes))
        frontier:list[MAZE.Edge] = [(first, choice(unvisited_neighbor_nodes(first)))]
        visited.add(first)
        animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=set(visited)))
        previous:MAZE.NodeId
        current:MAZE.NodeId
        while frontier:
            previous,current = frontier.pop()
            if current not in visited:
                next_nodes:list[MAZE.NodeId] = unvisited_neighbor_nodes(current)
                shuffle(next_nodes)
                next:MAZE.NodeId
                for next in next_nodes:
                    frontier.append((current, next))
                paths.add((previous, current))
                visited.add(current)
                animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=set(visited)))

        return Maze(paths, height_nodes, width_nodes)
    
    @staticmethod
    def GenerateFromWilsons(height_nodes:int, width_nodes:int, animator:Animator=NullAnimator()) -> MazeContract:

        def get_neighbor_nodes(node:MAZE.NodeId) -> list[MAZE.NodeId]:
            j,i = node
            nodes:MAZE.NodeId = set()
            if i < width_nodes - 1:
                nodes.add((j,i+1))
            if i > 0:
                nodes.add((j,i-1))
            if j < height_nodes - 1:
                nodes.add((j+1,i))
            if j > 0:
                nodes.add((j-1,i))
            return list(nodes)

        nodes:set[MAZE.NodeId] = set((j,i) for i in range(width_nodes) for j in range(height_nodes))

        paths:set[MAZE.Edge] = set()
        first_node:MAZE.NodeId = nodes.pop()
        maze_nodes:set[MAZE.NodeId] = {first_node}
        animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=set(maze_nodes)))
        while nodes:
            arb:MAZE.NodeId = nodes.pop()
            visited:list[MAZE.NodeId] = [arb]
            animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=(maze_nodes.union(set(visited)))))
            next_node:MAZE.NodeId = choice(get_neighbor_nodes(arb))
            while next_node not in maze_nodes:
                if next_node not in visited:
                    visited.append(next_node)
                    animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=(maze_nodes.union(set(visited)))))
                    next_node = choice(get_neighbor_nodes(next_node))
                else:
                    while visited.pop() != next_node:
                        animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=(maze_nodes.union(set(visited)))))
                        pass
            for i,node in enumerate(visited):
                maze_nodes.add(node)
                if node in nodes:
                    nodes.remove(node)
                next = next_node if i == len(visited) - 1 else visited[i+1]
                paths.add((node,next))
                animator.save_frame(Maze(set(paths), height_nodes, width_nodes, nodes=(maze_nodes.union(set(visited)))))

        return Maze(paths, height_nodes, width_nodes)
    

    @staticmethod
    def GenerateFromOriginShift(height_nodes:int, width_nodes:int, animator:Animator=NullAnimator()) -> MazeContract:

        class Node():
            def __init__(self, j,i):
                self.id = (j,i)
                if i < width_nodes-1:
                    self.pointer = (j,i+1)
                elif j < height_nodes-1:
                    self.pointer = (j+1,i)
                else:
                    self.pointer = None
            def __repr__(self):
                return f"id:{self.id}  pointer:{self.pointer}"
            
        def get_neighbor_nodes(node:MAZE.NodeId) -> list[MAZE.NodeId]:
            j,i = node
            nodes:MAZE.NodeId = set()
            if i < width_nodes - 1:
                nodes.add((j,i+1))
            if i > 0:
                nodes.add((j,i-1))
            if j < height_nodes - 1:
                nodes.add((j+1,i))
            if j > 0:
                nodes.add((j-1,i))
            return list(nodes)
        
        def reset_origin():
            origin_value = origin
            if choice(range(20)) == 10:
                _n = nodes[choice(list(nodes.keys()))]
                lst = list()
                while True:
                    lst.append(_n.id)
                    if _n.pointer == None:
                        break
                    _n = nodes[_n.pointer]
                lst.reverse()
                for i,node in enumerate(lst):
                    if i == len(lst)-1:
                        nodes[node].pointer = None
                        origin_value = nodes[node]
                    else:
                        nodes[node].pointer = lst[i+1]
            return origin_value
        
        def get_paths():
            paths = set()
            for node in nodes.keys():
                mynode = nodes[node]
                if mynode.pointer is not None:
                    paths.add((nodes[node].id,nodes[node].pointer))
            return paths


        nodes:dict[tuple[int,int],Node] = {(j,i):Node(j,i) for i in range(width_nodes) for j in range(height_nodes)}

        cycles = height_nodes*width_nodes*10
        origin = nodes[(height_nodes-1,width_nodes-1)]
        while cycles > 0:
            animator.save_frame(Maze(get_paths(), height_nodes, width_nodes))
            origin = reset_origin()
            next = choice(get_neighbor_nodes(origin.id))
            origin.pointer = next
            origin = nodes[next]
            origin.pointer = None
            cycles -= 1


        paths = get_paths()

        return Maze(paths, height_nodes, width_nodes, set(nodes.keys()))

