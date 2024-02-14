const inputText = document.getElementById("inputText");

//add elem
function newElement(){
    let li = document.createElement("li");
    let text = inputText.value;
    if(text === ""){
        alert("Enter task");
        return;
    }
    let input = document.createElement("input");
    input.setAttribute("type", "checkbox");
    input.className = "checkbox";
    input.addEventListener("click", completeTask)

    let span1 = document.createElement("span");
    span1.className = "text";
    span1.innerHTML = text;
    
    let span2 = document.createElement("span");
    span2.className = "delete"  ;
    span2.appendChild(document.createTextNode("\u00D7"))
    span2.addEventListener("click", deleteElement)

    let par = document.getElementById("ul")
    li.appendChild(input);
    li.appendChild(span1);
    li.appendChild(span2);
    par.appendChild(li);


    inputText.value = "";
}
document.getElementById("btn").addEventListener("click", newElement)

// complete task
function completeTask(event) {
    let checkbox = event.target;
    
    let textElement = checkbox.nextElementSibling;

    if (checkbox.checked) {
        textElement.style.textDecoration = "line-through";
    } else {
        textElement.style.textDecoration = "none";
    }
}

document.querySelectorAll('.checkbox').forEach(checkbox => {
    checkbox.addEventListener('change', completeTask);
});




// delete elem
function deleteElement(event) {
    let del = event.target.closest("li");
    del.parentNode.removeChild(del);
}

document.querySelectorAll('.delete').forEach(deleteButton => {
    deleteButton.addEventListener('click', deleteElement);
});