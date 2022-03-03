function modifyUI(es) {
    parent_ul = $('#es_list');

    // remove the loading indicator
    parent_ul.empty()

    // iterate and add the errors
    es.forEach(e => {
        child_template = `<li class="d-flex no-seen">
                        <div class="info">
                            <span href="" class="font-w600 mb-0 color-primary">
                                ${e.id}
                            </span>
                            <p class="pb-0 mb-0 line-h14 mt-6">
                                    ${e.title}
                            </p>
                        </div>
                    </li>`;
        parent_ul.append(child_template);
    });
}


// get the errors and modify the UI
async function initErrors() {
    fetch(`http://${mother}/error/get/${es_n}`)
        .then(res => res.json())
        .then((res) => {
            modifyUI(res.es);
        });

}

// delay the start to leave some window for populateMeanGraph()
setTimeout(initErrors, 1000 * 3);