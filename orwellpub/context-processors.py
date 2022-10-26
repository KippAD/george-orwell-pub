from django.contrib.auth import logout


def logout_form(request):
    return {
        'logout_form': logout,
    }