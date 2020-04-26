# For any successfull message a prefix 'success_' is must.
# For any failed      message a prefix 'fail_'    is must.
# For any info        message a prefix 'info_'    is must.

def success_valid_user(email):
    return f'Welcome back {email}!'


def fail_not_valid_credentials():
    return f'Login Unsuccessfully. Please check username and password.'


def fail_not_valid_email():
    return f'Login Unsuccessfully. Invalid email address.'


def fail_not_valid_password():
    return f'Login Unsuccessfully. Invalid password.'