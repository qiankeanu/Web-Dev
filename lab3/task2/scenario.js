document.addEventListener("DOMContentLoaded", function () {
    const engizu = document.getElementById("taskInput");
    const kosu = document.getElementById("addTask");
    const list = document.getElementById("taskList");
    const cnt = document.getElementsByClassName("counter")[0]

    let counter = 0;

    kosu.addEventListener("click", function () {
        const text = engizu.value.trim();
        if (text === "") return;

        const li = document.createElement("li");

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";

        checkbox.addEventListener("change", function () {
            span.classList.toggle("completed");
        });

        const span = document.createElement("span");
        span.textContent = text;

        const trashIcon = document.createElement("i");
        trashIcon.classList.add("fa", "fa-trash-o"); 
        trashIcon.addEventListener("click", function () {
            list.removeChild(li);
        });

        li.appendChild(checkbox);
        li.appendChild(span);
        li.appendChild(trashIcon);
        list.appendChild(li);
        
        counter++;

        cnt.innerHTML = counter;


        engizu.value = "";
    });
    
});
