# blog-flask-ssr

This the the repository for my personal blog to eventually publish my various papers. It uses an interesting technology stack including:

* ArrowJS:
  
  A reactive library with no build tools. Some of the benefits of component based rendering for organization while loading fast with cached js files. For things like forms, navbars, footers which don't change much it uses this
* HTMX:

  For Ajax rquests and learning a new library. For data requests and form input handling it uses this library.
* Flask:

  For learning a new static file web server that can make use of python's vast module library for data science in the future. Has nice support for form validation, login services, and connecting to the persistance layer.

This project supports a user system for multiple authors and comments. The contact me form can be used in the eventual implementation of the admin dashboard to control the role users have. 

TODO:
* Implement a series

Will require a custom search select option input for large number of post series.

