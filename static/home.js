function redirect()
{
    let room_name = document.getElementById("room-name-form").value;
    window.location.href = "/" + room_name;
}

function add_listener_for_enter()
{
    let room_name_form = document.getElementById("room-name-form");
    room_name_form.addEventListener(
        "keydown",
        function()
        {
            if (event.key === "Enter") redirect();
        });
}

function main()
{
    add_listener_for_enter();
}

window.onload = main();