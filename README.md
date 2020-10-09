# Shortest-Path Tree Finder

![Demo](https://raw.githubusercontent.com/samul-1/ro/main/demo.gif)

Given a graph, this script traverses it utilizing a breadth-first search (BFS) algorithm, outputting the resulting tree.

If the tree found by the visit is a shortest-path tree (SPT), the program terminates. If not, an SPT is built using a Bellman Ford-like algorithm and subsequently output.

The program will ask for the number *n* of nodes of the graph, and then will await *n* numbers to be input, each one followed by a newline, which will be the number labels of the nodes.

Afterwards, the user will be prompted for *m*, the number of edges. 3*m* lines are then to be input: for each edge, the program will expect the first number to be the label of the source node, then the destination node, and finally the cost of such edge.
All three numbers must be separated by a newline. For example, the edge from node 1 to node 2 with cost 3 is to be input like this:

```
1
2
3
```
## Requirements
For this program to work correctly, you will need the **networkx** and **matplotlib** libraries to be installed.
If you use **pip**, you can install those with the following two commands:

```
pip3 install networkx
pip3 install matplotlib
```


## Beware
- The current version of this program will only work correctly if there is a node named **1**. This will be used as the source for the BFS visit and will be the root of the tree.
A subsequent version of the program will allow users to specify different root nodes.
- The current version of this program will only work correctly if the input graph is connected. Unconnected parts will not be shown. If you need to use it with a graph that has nodes that are unreachable from node 1, you'll need to add fake edges manually. A later version of this program will take care of this.

Here's an example input you can use to try the program out yourself. *(This is the graph used during class, Oct 8th.)*

```
5
1
2
3
4
5
8
1
2
5
1
3
7
2
3
1
2
4
5
2
5
3
3
4
3
3
5
2
5
4
1
```
