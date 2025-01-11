// Edit constants
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment_body");
const commentTitle = document.getElementById("id_comment_title");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
 * Initializes edit functionality for the provided edit buttons.
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates `commentText` input/textarea with the comment's content for edit
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}/` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(
          `comment${commentId}`).innerText;
        commentText.value = commentContent;
        let commentTitleContent = document.getElementById(
            `comment${commentId}`).innerText;
        commentTitle.value = commentTitleContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}/`);
    });
}
