from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app


main_bp = Blueprint('main', __name__)
error_bp = Blueprint('error', __name__, url_prefix='/error')

# ================= ERROR HANDLERS =====================
@error_bp.app_errorhandler(404)
def handle_404(error):
    return render_template('errors/404.html'), 404


@error_bp.app_errorhandler(401)
def handle_401(error):
    return render_template('errors/401.html'), 401


# ============== Main Applications ==================

@main_bp.route('/')
def index():
    todoapp_server = current_app.config['TODO_APP_SERVER']
    eventapp_server = current_app.config['EVENT_APP_SERVER']
    blogapp_server = current_app.config['BLOG_APP_SERVER']

    return render_template('pages/index.html', todoapp_server=todoapp_server, eventapp_server=eventapp_server, blogapp_server=blogapp_server) 





