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

    .then(async response => {

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Schedule fetch failed");
        }

        const taskList = document.getElementById("taskList");
        taskList.innerHTML = "";

        data.forEach(task => {

            const li = document.createElement("li");

            li.innerHTML = `
                <strong>${task.subject}</strong><br>
                Topic: ${task.topic}<br>
                Deadline: ${task.deadline}<br>
                Priority: ${task.priority}
            `;

            taskList.appendChild(li);
        });

    })

    .catch(error => {
        console.error(error);
        alert("Error: " + error.message);
    });
}