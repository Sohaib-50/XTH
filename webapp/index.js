document.addEventListener("DOMContentLoaded", () => {
    
    display_posts();


});


function display_posts() {
    let posts;

    fetch('https://jsonplaceholder.typicode.com/posts/')
        .then((response) => response.json())
        .then((json) => {
            posts = json;

            // remove posts loading message
            let loading_message = document.querySelector("#loading-message");
            if (loading_message != null) {
                loading_message.remove();
            }

            // for each post get user info and then display the post and user details as a row
            posts.forEach(post => {
                let user;
                let userId = post["userId"];

                fetch(`https://jsonplaceholder.typicode.com/users/${userId}/`)
                    .then((response) => response.json())
                    .then((json) => {
                        user = json;
                        add_row(post, user);
                    });
            });

        });
}

function add_row(post, user) {
    let posts_div = document.querySelector("#posts");

    posts_div.innerHTML += (`
    <div class="posts-row">
        <div class="posts-row-cell">
            ${user.id}
        </div>
        <div class="posts-row-cell">
            ${post.id}
        </div>
        <div class="posts-row-cell">
            ${post.title.slice(0, 80) + "...."}
        </div>
        <div class="posts-row-cell">
            ${post.body.slice(0, 80) + "...."}
        </div>
        <div class="posts-row-cell">
            ${user.name}
        </div>
        <div class="posts-row-cell">
            ${user.username}
        </div>
        <div class="posts-row-cell">
            ${user.email}
        </div>
        <div class="posts-row-cell">
            ${user.address.street + ", " + user.address.city}
        </div>
        <div class="posts-row-cell">
            ${user.phone}
        </div>
        <div class="posts-row-cell">
            ${user.website}
        </div>
        <div class="posts-row-cell">
            ${user.company.name}
        </div>
    </div>`);
}