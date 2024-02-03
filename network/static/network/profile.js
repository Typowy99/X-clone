document.addEventListener('DOMContentLoaded', function() {
    const followBtn = document.querySelector('#follow-btn');
    const editBtnAll = document.querySelectorAll('[id^="edit-btn-"]');

    if (followBtn) {
        followBtn.addEventListener('click', function() {
            const username = this.dataset.username;

            fetch(`/follow/`, {
                method: 'POST',
                body: JSON.stringify({
                    username: username
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok');
                }
            })
            .then(data => {
                if (data && data.follow !== undefined) {
                    this.textContent = data.follow ? "Unfollow" : "Follow";
                } else {
                    throw new Error('Invalid response data received');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    if (editBtnAll) {
        editBtnAll.forEach(function(btn) {
            btn.addEventListener('click', function() {
                const postId = this.id.split('-')[2]; 
                const editFormAreaId = `edit-formarea-${postId}`;
                const postContentId = `post-content-${postId}`;
                const saveBtnId = `save-btn-${postId}`;
                const editTextareaId = `edit-textarea-${postId}`;

                const postContentElement = document.getElementById(postContentId);
                const editFormArea = document.getElementById(editFormAreaId);
                const saveBtn = document.getElementById(saveBtnId);
                const editTextarea = document.getElementById(editTextareaId);

                if (editFormArea) {
                    editFormArea.style.display = (editFormArea.style.display === 'block') ? 'none' : 'block';
                    postContentElement.style.display = (editFormArea.style.display === 'block') ? 'none' : 'block';
                }

                if (saveBtn) {
                    saveBtn.addEventListener('click', function() {
                        const editedContent = editTextarea.value;

                        fetch(`/edit_post/`, {
                            method: 'POST',
                            body: JSON.stringify({
                                post_id: postId,
                                post_content: editedContent
                            })
                        })
                        .then(response => {
                            if (response.ok) {
                                return response.json();
                            } else {
                                throw new Error('Network response was not ok');
                            }
                        })
                        .then(data => {
                            if (data) {
                                editFormArea.style.display = 'none';
                                postContentElement.style.display = 'block';
                                postContentElement.textContent = editedContent;
                            } else {
                                throw new Error('Invalid response data received');
                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });
                    });
                }
            });
        });
    }
});
