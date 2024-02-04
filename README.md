
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

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Run migrations:
```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

