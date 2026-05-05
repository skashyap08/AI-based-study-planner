function addTask() {
    const data = {
        subject: document.getElementById("subject").value,
        topic: document.getElementById("topic").value,
        difficulty: parseInt(document.getElementById("difficulty").value),
        deadline: document.getElementById("deadline").value
    };

    console.log("Sending:", data); // DEBUG

    fetch('/add_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        getSchedule(); // auto refresh
    })
    .catch(err => {
        console.error("Error:", err);
        alert("Error adding task");
    });
}


function getSchedule() {
    fetch('/schedule')
    .then(res => res.json())
    .then(data => {
        console.log("Schedule:", data); // DEBUG

        const list = document.getElementById("taskList");
        list.innerHTML = "";

        if (data.length === 0) {
            list.innerHTML = "<li>No tasks found</li>";
            return;
        }

        data.forEach(task => {
            const li = document.createElement("li");
            li.innerText = `${task.subject} - ${task.topic} | Priority: ${task.priority.toFixed(2)}`;
            list.appendChild(li);
        });
    })
    .catch(err => {
        console.error("Error:", err);
        alert("Error fetching schedule");
    });
}