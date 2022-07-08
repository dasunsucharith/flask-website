function deletePost(postID) {
    fetch("/delete-post", {
        method: "POST",
        body: JSON.stringify({ postID: postID }),
    }).then((_res) => {
        window.location.href = "/";
    })
}