from django.shortcuts import render
from random import randint
from algos import dijkstra as dj

ROW_COUNT = 30
COLUMN_COUNT = 50

# Create your views here.
def visualizer(request):
	if request.GET.get('algo') == 'dijkstra':
		graph = dj.Graph()
		origin = str(request.GET.get('start'))
		destination = str(request.GET.get('end'))
		splitted_start = request.GET.get('start').split('-')
		splitted_end = request.GET.get('end').split('-')
		startNode = (int(splitted_start[0]), int(splitted_start[1]))
		finishNode = (int(splitted_end[0]), int(splitted_end[1]))
		visited, path = dj.shortest_path(graph, origin, destination)
		print(path)
		path = " ".join(path)
		visited = " ".join(visited.keys())
		print(path)
		
		grid = {'rows': range(ROW_COUNT+1), 'columns': range(COLUMN_COUNT+1), 'startNode':startNode, 'finishNode':finishNode, 'visitedInOrder':visited, 'path':path}
		return render(request, 'visualizer/visualizer.html', grid)
	else:
		startNode = (randint(1,ROW_COUNT), randint(1,COLUMN_COUNT))
		print(startNode)
		finishNode = (randint(1,ROW_COUNT), randint(1,COLUMN_COUNT))
		while startNode == finishNode:
			finishNode = (randint(1,ROW_COUNT), randint(1,COLUMN_COUNT))
		grid = {'rows': range(ROW_COUNT+1), 'columns': range(COLUMN_COUNT+1), 'startNode':startNode, 'finishNode':finishNode}
		return render(request, 'visualizer/visualizer.html', grid)
	

