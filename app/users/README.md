# User Directory

Contains all the routes mapped in the controller as well as methods to verify:
* Is the user logged in
* Is the user's email verified
* Is the user an author
* Is the user an admin

Depending on the role the user will have access to post comments and use the contact me if a user, post and edit their own post if an author, access to edit and delete all users post as well as have access to management tools if they are an admin

Since flask has a lot of methods to handle users I am using this for handling it as security is something I don't trust myself to make sure it is up to date with all the attack methods. If you are doing a custom service it might be wise to move the authCheck.py methods to a service with your own implementation. This would be better for larger projects.