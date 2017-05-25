from flask import Blueprint
# from .views import EmployeesSingle, EmployeesUpdate, EmployeesDelete


urls = [
    ('/<string:id>', UserSingle, 'DepartmentsSingle'),
    ('/create', UserCreate, 'DepartmentsCreate'),
    ('/update/<string:id>', UserUpdate, 'DepartmentsUpdate'),
    ('', UsersList, 'DepartmentsList')
]

users = Blueprint('users', __name__)

for url_str, view_class, endpoint_name in urls:
    users.add_url_rule(url_str, view_func=view_class.as_view(endpoint_name))