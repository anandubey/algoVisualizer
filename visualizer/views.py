from django.shortcuts import render
from random import randint

ROW_COUNT = 30
COLUMN_COUNT = 50

# Create your views here.
def visualizer(request):
	startNode = (randint(1,ROW_COUNT), randint(1,COLUMN_COUNT))
	finishNode = (randint(1,ROW_COUNT), randint(1,COLUMN_COUNT))
	while startNode == finishNode:
		finishNode = (randint(1,ROW_COUNT), randint(1,COLUMN_COUNT))
	print(startNode, finishNode)
	grid = {'rows': range(ROW_COUNT+1), 'columns': range(COLUMN_COUNT+1), 'startNode':startNode, 'finishNode':finishNode}
	return render(request, 'visualizer/visualizer.html', grid)
