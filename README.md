# BlogAPI
Django API for Blog! You can use this API to create your blog. 

---


## Users

### /api/v1/register/
Method: `POST`
User Registeration. `username` , `email` and `password` required.

### /api/v1/token/
Method: `POST`
Get access token and refresh token.

### /api/v1/token/refresh/
Method: `POST`
Refresh token.

### /api/v1/verify-email/
Method: `GET`
when you register a user, he will receive an email. He can use that email to verify his account. Here API will get tokens and verify the account.

### /api/v1/resetpassword/
Method: `POST`
Request for reset password. The link will send to the user's email address.

### /api/v1/changepassword/
Method: `POST`
Change user's password.

### /api/v1/logout/
Method: `POST`
Add user's token to the blacklist.


---

## Blog
### /api/v1/blog/list/
Method: `GET`
List of  posts.

### /api/v1/blog/show/id/
Method: `GET`
Show post by id.

### /api/v1/blog/create/
Method: `POST`
Create post.


### /api/v1/blog/delete/id/
Method: `DELETE`
Delete post by id.


### /api/v1/blog/update/id/
Method: `PUT`
Update post by id.


### /api/v1/blog/like/save/
Method: `POST`
Save like for posts.

### /api/v1/blog/like/show/id/
Method: `GET`
Show like for each post by id.

### /api/v1/blog/comment/list/
Method: `GET`
List of  comments.

### /api/v1/blog/comment/show/id/
Method: `GET`
Show comments by id.

### /api/v1/blog/comment/create/
Method: `POST`
Create comment.


### /api/v1/blog/comment/delete/id/
Method: `DELETE`
Delete comments by id.


### /api/v1/blog/comment/update/id/
Method: `PUT`
Update comment by id.

