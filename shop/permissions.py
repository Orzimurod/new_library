from django.contrib.auth.decorators import user_passes_test


# def not_salesman(user):
#     salesmen = Group.objects.get(name='Sotuvchilar')
#     return user.is_authenticated and salesmen not in user.groups.all()


# def new_order_permission(view_func=None, login_url=None):
#     actual_decorator = user_passes_test(
#         lambda u: not_salesman(u),
#         login_url=login_url,
#     )


#     if view_func:
#         return actual_decorator(view_func)
#     return actual_decorator


def admin(user):
    return user.is_authenticated and user.username == 'admin'


def new_order_permission(view_func=None, login_url=None):
    actual_decorator = user_passes_test(
        lambda u: admin(u),
        login_url=login_url,
    )

    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
