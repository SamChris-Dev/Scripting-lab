
function addCar() {
    const name = prompt("Enter Car name:");

    if (name) {
        const listItem = document.createElement("li");
        listItem.textContent = name;
        studentList.appendChild(listItem);
    }
}
