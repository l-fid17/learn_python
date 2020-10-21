from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


posts = {
    0: {
        "id": 0,
        "title": "Post One",
        "content": "Content of the post"
    },
    1: {
        "id": 1,
        "title": "Post Two",
        "content": "Content of the post"
    }
}


@app.route('/')
def home():
    return render_template("home.jinja2", posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template("not_found.jinja2", message=f"Post {post_id} not found.")
    return render_template("post.jinja2", post=post)

@app.route('/post/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {"id": post_id, "title": title, "content": content}
        return redirect("/")
    return render_template("create.jinja2")



if __name__ == "__main__":
    app.run(debug=True)