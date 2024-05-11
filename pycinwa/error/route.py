from flask import Blueprint, render_template

error = Blueprint('error', __name__, static_folder='static', template_folder='templates',
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
    # TODO: params
    return render_template("error.html",
                           error_name="Error", error_description="Error description :D")
