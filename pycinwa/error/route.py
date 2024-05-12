from flask import Blueprint, render_template, request

error = Blueprint('error', __name__, static_folder='static',
                  template_folder='templates',
                  url_prefix='/error')


@error.get('/')
def load_error():
    """
    Load error page

    Returns
    -------
    The error page, with the following content:
    error_name: the name of the error
    error_description: the description of the error
    """
    args = request.args
    return render_template("error.html",
                           error_name=args.get('name'),
                           error_description=args.get('description'))
