from collections import deque

# Breadth-first search function
def bfs(root_node, goal_value):
  path_queue = deque()
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  while path_queue:
    current_path = path_queue.pop()
    current_node = current_path[-1]
    if current_node.value == goal_value:
      return current_path
    
    for child in current_node.children:
      newpath = current_path[:]
      newpath.append(child)
      path_queue.appendleft(newpath)

  return None
  
    
  

 