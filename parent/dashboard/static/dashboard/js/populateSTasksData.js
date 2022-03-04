function populateSTasksData() {
    t_c_t = document.querySelector("#total-complete-today")
    c_l_w = document.querySelector("#cmp-last-week")

    clw = Math.floor((wst / lwst) * 100) - 100

    if (clw > 0) {
        clw_prefix = "+"
    } else {
        clw_prefix = "-"
    }

    c_l_w.innerText = `${clw_prefix}${Math.abs(clw)}% `
    t_c_t.innerText = `${Math.floor((rtst / stst) * 100)}% `
}

setTimeout(populateSTasksData, 2)