function join_room()
{
    let room_name = document.getElementById("room-name").innerText;
    socket.emit("join", room_name);
    request_biggest_id();
}

function update_loading_older_comments_icon()
{
    let loading_icon = document.getElementById("loading-icon"); 
    if (smallest_loaded_id > smallest_requested_id)
    {
        loading_icon.style.display = "block";
    }
    else loading_icon.style.display = "none";
}

function request_biggest_id()
{
    let room_name = document.getElementById("room-name").innerText;
    socket.emit("request_biggest_id", room_name)
}

function handle_biggest_id(response)
{
    let biggest_id = response.id;
    // if no comments posted in room
    if (biggest_id === 0);
    // if there are comments posted but none are loaded in client
    else if (smallest_requested_id === Infinity)
    {
        // request the newest comment
        request_comments(biggest_id, biggest_id);
    }
    // if client didn't recieve newer comments
    else if (biggest_id > biggest_loaded_id)
    {
        // request newer missing comments
        request_comments(biggest_id, biggest_loaded_id + 1);
    }
}

function request_comments(biggest_id, smallest_id)
{
    let room_name = document.getElementById("room-name").innerText;
    let request = 
    {
        "room_name": room_name,
        "biggest_id": biggest_id,
        "smallest_id": smallest_id
    };
    socket.emit("comments_request", request);
    smallest_requested_id = Math.min(smallest_id, smallest_requested_id)
}

function get_older_comments(num_of_comments_to_load)
{
    // if scrollbar reaches the top, load older comments
    let comment_section = document.getElementById("comment-section");
    let num_of_comments = document.getElementsByClassName("comment").length;
    if 
    (
        comment_section.scrollTop === 0 &&
        num_of_comments > 0 &&
        smallest_loaded_id > 1 &&
        smallest_requested_id === smallest_loaded_id
    )
    {
        let id_a = smallest_loaded_id - 1;
        let id_b = Math.max(smallest_loaded_id - num_of_comments_to_load, 1);
        request_comments(id_a, id_b);
    }
    update_loading_older_comments_icon();
}

function create_comment_element(comment)
{
    let new_comment = document.createElement("div");
    new_comment.classList.add("comment");
    new_comment.id = comment.in_room_id;
    new_comment.innerText = comment.text;
    return new_comment;
}

function insert_comment(new_comment)
{
    let comment_section = document.getElementById("comment-section");
    let comments = document.getElementsByClassName("comment");
    let dist_from_bottom = comment_section.scrollHeight - comment_section.scrollTop;
    let old_scroll_top = comment_section.scrollTop;
    // with WebSocket messages are guaranteed to be in order
    // BUT socketio falls back on other protocols that do not guarantee it

    // insert comment before the first comment in comment section that is newer
    for (let i = 0; i < comments.length; i++)
    {
        if (parseInt(comments[i].id) > parseInt(new_comment.id))
        {
            comments[i].before(new_comment);
            comment_section.scrollTop = comment_section.scrollHeight - dist_from_bottom;
            return;
        }
    }
    // if new_comment is newer than all other comments in comment section append it
    let scrolled_to_bottom = comment_section.scrollHeight - comment_section.scrollTop === comment_section.clientHeight
    comment_section.appendChild(new_comment);
    if (scrolled_to_bottom)
    {
        // scroll back to the bottom
        comment_section.scrollTop = comment_section.scrollHeight - comment_section.clientHeight;
    }
    else
    {
        comment_section.scrollTop = old_scroll_top;
    }
}

function update_comment_section(new_comments)
{
    for (let new_comment of new_comments)
    {
        insert_comment(create_comment_element(new_comment));
        smallest_loaded_id = Math.min(new_comment.in_room_id, smallest_loaded_id);
        biggest_loaded_id = Math.max(new_comment.in_room_id, biggest_loaded_id);
    }
    // jump to the last viewing position after it was pushed down when inserting comment
}

function send_comment()
{
    let comment_section = document.getElementById("comment-section");
    let text = document.getElementById("comment-form").value;
    let room_name = document.getElementById("room-name").innerText;
    document.getElementById("comment-form").value = "";
    socket.emit
    (
        "new_comment",
        { text: text, room_name: room_name }
    );
    // scroll to the bottom
    comment_section.scrollTop = comment_section.scrollHeight - comment_section.clientHeight;
}

function add_listener_for_send_by_enter()
{
    let comment_form = document.getElementById("comment-form");
    comment_form.addEventListener
    (
        "keydown",
        function(event) { if (event.key === "Enter") send_comment(); }
    );
}

function add_listener_for_send_by_click()
{
    let send_icon = document.getElementById("send-button");
    send_icon.addEventListener("click", send_comment);
}

var socket = io();
var smallest_requested_id = Infinity;
var smallest_loaded_id = Infinity;
var biggest_loaded_id = -Infinity;

function main()
{
    socket.on("update_comment_section", update_comment_section);
    socket.on("biggest_id", handle_biggest_id);
    socket.on("connect", join_room);
    setInterval(get_older_comments, 1000, 15);
    add_listener_for_send_by_enter();
    add_listener_for_send_by_click();
}

document.addEventListener
(
    "DOMContentLoaded", 
    function(event) { main(); }
);