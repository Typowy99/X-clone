document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#follow-btn').onclick = function() {
        
        //add username to variable
        username = this.dataset.username

        //follow or unfollow user
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
                console.error('Network response was not ok')
            }
        })
        .then(data => {
            if (data.follow) {
                this.textContent = "Unfollow"
            } else {
                this.textContent = "Follow"
            }
        })
        .catch(error => {
            console.error('Error:', error);
          });
    }
});