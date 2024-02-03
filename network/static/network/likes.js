document.addEventListener('DOMContentLoaded', function() {
    const likesBtn = document.querySelectorAll('[id^="like-btn-"]');

    likesBtn.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const postId = this.id.split('-')[2]; 

            fetch(`/like_post/`, {
                method: 'POST',
                body: JSON.stringify({
                    post_id: postId,
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
                const likeCountIcon = document.querySelector(`#like-btn-${postId} i.fa-heart`);
                const likeCountText = document.querySelector(`#likes-count-${postId}`);
                
                if (data.like) {
                    likeCountIcon.classList.remove('fa-regular');
                    likeCountIcon.classList.add('fa-solid');
                } else {
                    likeCountIcon.classList.remove('fa-solid');
                    likeCountIcon.classList.add('fa-regular');
                }
                likeCountText.textContent = data.likes_count;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        })
    })
});