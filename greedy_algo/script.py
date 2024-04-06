import random
from random import randrange
from Graph import Graph
from Vertex import Vertex


def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g


def helper(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex]=='unvisited':
      return False
  return True 
def traveling_saleperson(graph):
  final_path = ""
  visited_vertice= {x : "unvisited" for x in graph.graph_dict}
  current_vertex = random.choice(list(graph.graph_dict))
  visited_vertice[current_vertex]= 'visited'
  final_path += current_vertex
  check_visited= helper(visited_vertice)
  while not check_visited:
    current_vertex_edge = graph.graph_dict[current_vertex].get_edges()
    current_vertex_weight= {}
    for edge in current_vertex_edge:
      current_vertex_weight[edge]= graph.graph_dict[current_vertex].get_edge_weight(edge)

    found_vertex = False
    next_vertex = ""
    while not found_vertex:
      if current_vertex_weight is None:
        check_visited = True 
      else:
        next_vertex = min(current_vertex_weight, key= current_vertex_weight.get)
        if visited_vertice[next_vertex] =='unvisited':
          found_vertex= True
          current_vertex= next_vertex
          visited_vertice[current_vertex] ="visited"
          final_path += current_vertex
        else:
          current_vertex_weight.pop(next_vertex)
    check_visited = helper(visited_vertice)
  print(final_path)


graph = build_tsp_graph(False)
traveling_saleperson(graph)