# Posts
Directory for post's model, controller, service and forms
## Post model
### id : int
        post object identifier
### title : string
        Blog post title
### content : text
        user inputted text
### htmlContent : text
        Reformatted text for display considering putting the logic for this in the script tag in the html file that is returned from the hx-get request
### published_at : DateTime 

        Date the post was created.
### updated_at : DateTime

        Date the post was last edited
## Post Controller
### **post()** : posts a post object 
    @postsBlueprint.route('/post', methods=['POST'])
    @author_required
    def post():
        form = PostForm()
        if form.validate_on_submit():
            post = createPost(title=form.title.data, content=form.content.data)
            return jsonify(post.toDictionary()), 201 
        return jsonify({"error": "Validation failed", "errors": form.errors}), 400
### **posts_list()** : returns list of post objects
    @postsBlueprint.route('/render/post', methods=['GET'])
    def posts_list():
        try:
            posts = getAllPosts()
            if posts is None:
                return jsonify({"error": "could not fetch posts"}), 400
            return ''.join(render_template('htmx/post.html', post=post) for post in posts)
            #return jsonify([post.toDictionary() for post in posts]), 200
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({"error": "An error occurred"}), 500