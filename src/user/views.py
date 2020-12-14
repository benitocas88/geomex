from admin.api import Blueprint

user = Blueprint('user', __name__)


@user.route('/sign-up', method=['GET'])
def sign_up():
    pass
