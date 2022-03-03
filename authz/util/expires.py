from datetime import timedelta

from authz.config import Config
from authz.util.now import now

def user_expires_at():
    return now() +timedelta(days=Config.USER_DEFAULT_EXPIRY_TIME)
    
