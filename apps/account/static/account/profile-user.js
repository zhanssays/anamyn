$(document).ready(function (e) {

    $("#add-child-btn").on("click", function (e) {
        var form = document.getElementById("add-child-form");
        var btn = document.getElementById("add-child-btn");
        var children_list = document.getElementById("children-list");
        form.style.display = "block";
        btn.style.display = "none";
        children_list.style.display = "none";
    });

    function children_list(){
        var form = document.getElementById("add-child-form");
        var btn = document.getElementById("add-child-btn");
        var children_list = document.getElementById("children-list");
        form.style.display = "none";
        btn.style.display = "block";
        children_list.style.display = "block";
    }

    $("#cancel-add-child").on("click", function (e) {
        children_list();
    });

    $("#planning-child-save-btn").on("click", function (e) {
        // var form = document.getElementById("planning-child-form");
        // var children_list = document.getElementById("planning-child-list");
        // form.style.display = "none";
        // children_list.style.display = "block";
        var planning_baby_checkbox = $('#planning_baby_checkbox').is(":checked");
        var pregnant_checkbox = $('#pregnant_checkbox').is(":checked");
        var weeks = $("#weeks_baby option:selected").val();
        var week = weeks.split(' ');
        week = Number(week[0]);
        var days = $("#days_baby option:selected").val();
        var day = days.split(' ');
        day = Number(day[0]);
        var date_birth_baby = $("#date-birth-baby").val();
        var children_selection = $("#children_selection option:selected").val();
        if (planningchild_id > 0) {
            $.ajax({
                url: url_planningchild_detail,
                type: "PUT",
                dataType: "json",
                data: {
                    planning: planning_baby_checkbox,
                    pregnant: pregnant_checkbox,
                    weeks: week,
                    days: day,
                    date_birth_baby: date_birth_baby,
                    children: children_selection
                },
                success: function () {
                    console.log('planning PUT saved');
                }
            });
            show_baby_planning();
        }
        else {
            $.ajax({
                url: url_planningchild_list,
                type: "POST",
                dataType: "json",
                data: {
                    planning: planning_baby_checkbox,
                    pregnant: pregnant_checkbox,
                    weeks: week,
                    days: day,
                    date_birth_baby: date_birth_baby,
                    children: children_selection,
                    user: user_id
                },
                success: function () {
                    console.log('planning POST saved');
                    location.reload();
                }
            });
        }


    });

    function show_baby_planning() {
        var form = document.getElementById("planning-child-form");
        var children_list = document.getElementById("planning-child-list");
        form.style.display = "none";
        children_list.style.display = "block";
    }

    function show_baby_planning_edit() {
        var form = document.getElementById("planning-child-form");
        var children_list = document.getElementById("planning-child-list");
        form.style.display = "block";
        children_list.style.display = "none";
    }

    if (is_user_planning_child_or_pregnant) {
        show_baby_planning();
    }
    else {
        show_baby_planning_edit();
    }

    $("#baby-planning-edit-btn").on("click", function (e) {
        e.preventDefault();
        show_baby_planning_edit()
    });

    $("#save-personal-inf-btn").on("click", function (e) {
        e.preventDefault();
        var first_name = $("#user_first_name_input").val();
        var last_name = $("#user_last_name_input").val();
        var date_of_birth = $("#user_date_input").val();
        var hide_age = $('#user_hide_age_checkbox').is(":checked");
        var email = $("#user_email_input").val();

        var city = $("#user_city option:selected").val();

        var marriage_status = $("#user_marriage_status option:selected").val();

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
                $.ajax({
                    url: url_user_detail,
                    type: "PUT",
                    dataType: "json",
                    data: {
                        first_name: first_name,
                        last_name: last_name,
                        email: email,
                    },
                    success: function () {
                    }
                });
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });


    });


    $("#add_child_save_btn").on("click", function (e) {
        //e.preventDefault();
        var child_name = $("#child_name_input").val();
        var child_date = $("#child_date_input").val();
        var gender = $('input[name=gender]:checked').val();
        var child_description = $("#child_description").val();
        var child_city = $("#child_city option:selected").val();
        var child_hospital = $("#child_hospital option:selected").val();
        var home_birth = $('#not_hospital').is(":checked");
        var hospital_rating = $(".star-rating input[type=radio]:checked ~ label").length;
        var hospital_review = $("#hospital_review").val();

        $.ajax({
                url: url_children_list,
                type: "POST",
                dataType: "json",
                data: {
                    user: user_id,
                    name: child_name,
                    child_date_birth: child_date,
                    gender: gender,
                    child_description: child_description,
                    city: child_city,
                    hospital: child_hospital,
                    home_birth: home_birth,
                    hospital_rating: hospital_rating,
                    hospital_description: hospital_review,
                },
                success: function () {
                    console.log('child saved');
                    children_list();
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