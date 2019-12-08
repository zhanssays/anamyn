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
    console.log(url_profile_list);
    $("#save-personal-inf-btn").on("click", function (e) {
        e.preventDefault();
        var first_name = $("#user_first_name_input").val();
        var last_name = $("#user_last_name_input").val();
        var date_of_birth = $("#user_date_input").val();
        var hide_age = $('#user_hide_age_checkbox').is(":checked");
        var email = $("#user_email_input").val();

        var city = $("#user_city option:selected").val();

        var marriage_status = $("#user_marriage_status option:selected").val();

        date_of_birth = new Date(date_of_birth).toISOString().slice(0, 10);

        console.log(first_name);
        console.log(last_name);
        console.log(date_of_birth);
        console.log(hide_age);
        console.log(email);
        console.log(city);
        console.log(marriage_status);


        $.ajax({
            url: url_profile_detail,
            type: "PUT",
            dataType: "json",
            data: {
                city: city,
                date_of_birth: date_of_birth,
                marriage_status: marriage_status,
                hide_age: hide_age,
            },
            success: function () {
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });



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