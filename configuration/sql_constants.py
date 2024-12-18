CONFIRM_EMAIL_BY_USER_EMAIL = '''
UPDATE users SET is_email_confirmed = true
WHERE email = %(email)s
'''
CONFIRM_PHONE_BY_USER_EMAIL = '''
UPDATE users SET is_phone_number_confirmed = true
WHERE email = %(email)s
'''
GET_USER_EMAIL_PHONE_CONFIRMED = '''
SELECT is_email_confirmed, is_phone_number_confirmed from users
WHERE email = %(email)s
'''