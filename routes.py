from config import app
from controller_functions import index, register, login, logout, dashboard, new_post, show_post, update_post, delete_post, add_like

app.add_url_rule("/", view_func=index)
app.add_url_rule("/users/create", methods=["POST"], view_func=register)
app.add_url_rule("/users/login", methods=["POST"], view_func=login)
app.add_url_rule("/logout", view_func=logout)
app.add_url_rule("/dashboard", view_func=dashboard)
app.add_url_rule("/posts/create", methods=["POST"], view_func=new_post)
app.add_url_rule("/posts/<post_id>/show", view_func=show_post)
app.add_url_rule("/posts/<post_id>/update", methods=["POST"], view_func=update_post)
app.add_url_rule("/posts/<post_id>/delete", view_func=delete_post)
app.add_url_rule("/likes/<post_id>", view_func=add_like)
