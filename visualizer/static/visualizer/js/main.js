function initializeMainNodes(startNode, endNode) {

	startNode.classList.add('startNode');
	var startItem = document.createElement('div');
	startItem.id = 'start_item';
	startItem.className = 'fill';
	startItem.draggable = 'true';
	startNode.appendChild(startItem);

	endNode.classList.add('endNode');
	var endItem = document.createElement('div');
	endItem.id='end_item';
	endItem.className = 'fill';
	endItem.draggable = 'true';
	endNode.appendChild(endItem);
}



function nodesDragger(){
	const startItem = document.getElementById('start_item');
	const endItem = document.getElementById('end_item');
	const empties = document.querySelectorAll('.empty');
	var startDragging = false;
	var endDragging = false;

	// Start Node Listener
	startItem.addEventListener('dragstart', startDragStart);
	startItem.addEventListener('dragend', startDragEnd);

	// End Node Listener
	endItem.addEventListener('dragstart', endDragStart);
	endItem.addEventListener('dragend', endDragEnd)


	// Event Listener for all the table cells
	for(const empty of empties){
		empty.addEventListener('dragover', dragOver);
		empty.addEventListener('dragenter', dragEnter);
		empty.addEventListener('dragleave', dragLeave);
		empty.addEventListener('drop', dragDrop);
	}


	// Drag functions for start node
	function startDragStart(){
		setTimeout(() => (this.className = 'invisible'), 0);
		startDragging=true;
	}

	function startDragEnd() {
		this.className = 'fill';
		startDragging = false;
	}

	// Drag functions for End node
	function endDragStart() {
		setTimeout(() => (this.className = 'invisible'), 0);
		endDragging = true;
	}

	function endDragEnd() {
		this.className = 'fill';
		endDragging = false;
	}

	//Handle Drag over empties
	function dragOver(e) {
		e.preventDefault();
	}

	function dragEnter(e) {
		e.preventDefault();
		this.className += 'hovered';
	}

	function dragLeave() {
		this.className = 'empty';
	}

	function dragDrop() {
		this.className = 'empty';
		if (startDragging) {
			this.append(startItem);
			document.getElementById('visualizeButton').href = "/?algo=dijkstra&start="+startItem.parentNode.id+"&end="+endItem.parentNode.id;
		}
		if(endDragging){
			this.append(endItem);
			document.getElementById('visualizeButton').href = "/?algo=dijkstra&start="+startItem.parentNode.id+"&end="+endItem.parentNode.id;
		}
		
	}
}


async function visualizeAlgorithm(visitedNodes, path, endNode){
	console.log(endNode);
	for (var i = 0; i < visitedNodes.length; i++) {
		if (visitedNodes[i] == endNode) {
			console.log("found");
			break;
		}
		var node = document.getElementById(visitedNodes[i]);	
		node.className = "visited";
		await new Promise(r => setTimeout(r, 20));

	}

	for (var i = 0; i < path.length; i++) {
		var node = document.getElementById(path[i]);
		node.className = "node-shortest-path";
		await new Promise(r => setTimeout(r, 20));
	}

}
