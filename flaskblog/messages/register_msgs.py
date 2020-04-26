# For any successfull message a prefix 'success_' is must.
# For any failed      message a prefix 'fail_'    is must.
# For any info        message a prefix 'info_'    is must.

def success_account_created():
    return 'Your account has been created! You are now able to log in.'

def failed_existed_username():
    return 'This username is currently taken. Please choose a different one.'

def failed_existed_email():
    return 'This email is currently taken. Please choose a different one.'