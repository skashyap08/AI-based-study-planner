function showToast(message, type = "success") {
    const container = document.getElementById("toast-container");

    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.innerText = message;

    container.appendChild(toast);

    setTimeout(() => toast.classList.add("show"), 100);

    setTimeout(() => {
        toast.classList.remove("show");
        setTimeout(() => container.removeChild(toast), 400);
    }, 3000);
}


function addTask() {
    const data = {
        subject: document.getElementById("subject").value,
        topic: document.getElementById("topic").value,
        difficulty: parseInt(document.getElementById("difficulty").value),
        deadline: document.getElementById("deadline").value
    };

    console.log("Sending:", data);

    fetch('/add_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        showToast("✅ " + data.message, "success");
        getSchedule(); // auto refresh
    })
    .catch(err => {
        console.error("Error:", err);
        showToast("❌ Error adding task", "error");
    });
}


function getSchedule() {
    const btn = document.getElementById("generateBtn");

    // 🔄 START loading state
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="loader"></span> Generating...';
    }

    fetch('/schedule')
    .then(res => res.json())
    .then(data => {
        console.log("Schedule:", data);

        const list = document.getElementById("taskList");
        list.innerHTML = "";

        if (data.length === 0) {
            list.innerHTML = "<li>No tasks found</li>";
        } else {
            data.forEach(task => {
                const li = document.createElement("li");
                li.innerText = `${task.subject} - ${task.topic} | Priority: ${task.priority.toFixed(2)}`;
                list.appendChild(li);
            });

            // 🎉 success toast after schedule loads
            showToast("📅 Smart plan generated!", "success");
        }

        // ✅ STOP loading state
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = "Generate Smart Plan";
        }
    })
    .catch(err => {
        console.error("Error:", err);
        showToast("❌ Error fetching schedule", "error");

        // ❌ Reset even if error
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = "Generate Smart Plan";
        }
    });
}