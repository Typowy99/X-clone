
# My Social Network

![Logo](https://i.imgur.com/98GafBp.png)


This project is a clone of the X social network, implemented using Python with the Django framework, JavaScript, HTML, CSS and Bootstrap. It allows users to make posts, follow other users, and "like" posts.

## Features

- New Post: Users can write new text-based posts by filling in text into a text area and then submitting the post.
- All Posts: Users can view all posts from all users, with the most recent posts appearing first. Each post includes the username of the poster, the post content, the date and time of the post, and the number of likes.
- Profile Page: Clicking on a username loads that user’s profile page, displaying the number of followers, the number of people the user follows, and all posts in reverse chronological order. Other users can choose to follow or unfollow this user.
- Following: Users can view all posts made by users they follow. Pagination is implemented to display posts 10 per page.
- Edit Post: Users can edit their own posts by clicking an "Edit" button and saving the edited post without requiring a page reload.
- Like and Unlike: Users can toggle whether they "like" a post asynchronously without reloading the entire page.



## Run Locally

1. **Clone the project**:
    ```
    git clone https://link-to-project
    ```

2. **Go to the project directory**:
    ```
    cd my-project
    ```

3. **Build Docker image** (if not built already):
    ```
    docker-compose build
    ```

4. **Run migrations**:
    ```
    docker-compose run web python manage.py migrate
    ```

5. **Start the server**:
    ```
    docker-compose up
    ```

After completing these steps, the application should be available locally at the address and port configured in the `docker-compose.yml` file. Users who have downloaded the project can now interact with the application running in the Docker container.



