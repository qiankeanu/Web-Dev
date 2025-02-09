document.addEventListener("DOMContentLoaded", function () {
    const taskInput = document.getElementById("taskInput");
    const addTaskButton = document.getElementById("addTask");
    const taskList = document.getElementById("taskList");

    addTaskButton.addEventListener("click", function () {
        const taskText = taskInput.value.trim();
        if (taskText === "") return;

        const li = document.createElement("li");

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.addEventListener("change", function () {
            li.classList.toggle("completed");
        });

        const span = document.createElement("span");
        span.textContent = taskText;

        // Заменяем кнопку на FontAwesome иконку
        const trashIcon = document.createElement("i");
        trashIcon.classList.add("fa", "fa-trash-o");
        trashIcon.style.fontSize = "25px"; // Размер иконки
        trashIcon.style.color = "red"; // Цвет
        trashIcon.style.cursor = "pointer"; // Курсор при наведении
        trashIcon.style.marginLeft = "10px"; // Отступ слева
        trashIcon.addEventListener("click", function () {
            taskList.removeChild(li);
        });

        li.appendChild(checkbox);
        li.appendChild(span);
        li.appendChild(trashIcon);
        taskList.appendChild(li);

        taskInput.value = "";
    });
});
