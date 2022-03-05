// Globals
const btnNewTask = $("#new-task-btn")
const btnCloseNewTask = $("#close-new-task-wizard")

// on submit do the processing
$("#new-task-form").submit(e => {
    // prevent page from loading
    e.preventDefault();

    // construct the request body
    const form = {
        name: $("#new-smart-name").val(),
        cron: $("#new-cron").val(),
        data: $("#new-smart-data").val()
    }

    // construct the request object
    const requestNewSTask = new Request(
        "/smarttasks/new", {
            method: 'POST',
            mode: 'same-origin',
            body: JSON.stringify(form),
        }
    );

    // request and process the response
    fetch(
        requestNewSTask
    ).then(res => {
        // parse the json response 
        return res.json();
    }).then(j => {
        console.log(j);
    });

    // close the wizard
    btnCloseNewTask.click();
});

// attach event listeners to the DOM elements