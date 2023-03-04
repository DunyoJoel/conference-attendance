from app.utils.config import settings
class User:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    ADMIN = {
        "admin_name": settings.ADMIN_NAME,
        "email": settings.ADMIN_EMAIL,
        "password": settings.ADMIN_PASSWORD,
        "contact": settings.ADMIN_CONTACT
        

    }