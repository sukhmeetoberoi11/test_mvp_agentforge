import redis
from .settings import settings


def get_redis_connection():
    return redis.StrictRedis.from_url(settings.redis_url)
