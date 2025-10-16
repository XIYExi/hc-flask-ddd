from domain.services.password_encoder import verify_password

def verify():
    data = verify_password()
    json = {
        'user': 'xiye',
        'message': 'pass by application.user_service',
        'domain': data
    }
    return json