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
DELETE_APPLICATIONS = '''
DELETE FROM applications
WHERE work_scope = %(work_scope)s 
'''
DELETE_COMPANIES = '''
DELETE FROM companies 
WHERE company_id = (
    SELECT company_id 
    FROM company_members_association 
    WHERE user_id = (
        SELECT id 
        FROM users 
        WHERE email = %(email)s
    )
);
'''


