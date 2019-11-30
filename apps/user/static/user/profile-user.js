$(document).ready(function (e) {

    $("#add-child-btn").on("click", function (e) {
        var form = document.getElementById("add-child-form");
        var btn = document.getElementById("add-child-btn");
        var children_list = document.getElementById("children-list");
        form.style.display = "block";
        btn.style.display = "none";
        children_list.style.display = "none";
    });

    $("#cancel-add-child").on("click", function (e) {
        var form = document.getElementById("add-child-form");
        var btn = document.getElementById("add-child-btn");
        var children_list = document.getElementById("children-list");
        form.style.display = "none";
        btn.style.display = "block";
        children_list.style.display = "block";
    });

    $("#planning-child-save-btn").on("click", function (e) {
        var form = document.getElementById("planning-child-form");
        var children_list = document.getElementById("planning-child-list");
        form.style.display = "none";
        children_list.style.display = "block";
    });

    $("#baby-planning-edit-btn").on("click", function (e) {
        e.preventDefault();
        var form = document.getElementById("planning-child-form");
        var children_list = document.getElementById("planning-child-list");
        form.style.display = "block";
        children_list.style.display = "none";
    });


    // $(".add-child-clone-btn").on("click", function (e) {
    //     var copy = document.querySelector("#add-child-form").cloneNode(true);
    //     // child_add_clone_count += 1;
    //     // copy.setAttribute("id", "add-child-form"+child_add_clone_count.toString());
    //     console.log("worked");
    //     console.log(copy);
    //
    //     const buttons = document.querySelectorAll('.add-child-clone-btn');
    //     for (const button of buttons) {
    //         button.addEventListener('click', this);
    //     }
    //     console.log(buttons);
    //
    //     var nav_children_tab = document.getElementById('nav-children');
    //     nav_children_tab.appendChild(copy);
    // });

});