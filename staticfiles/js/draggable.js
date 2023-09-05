function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    var draggedElement = document.getElementById(data);
    var square = event.target;

    if (square.id === "square") {
        square.appendChild(draggedElement);
        square.classList.add("green");
        document.getElementById("doneMessage").style.display = "block";
        document.getElementById("info").style.display = "none";
        draggedElement.style.top = "0";
        draggedElement.style.left = "0";
    }
}