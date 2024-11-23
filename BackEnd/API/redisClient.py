# redisClient.py

import redis
from typing import Optional
from datetime import datetime, timedelta


# Configuration Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def get_redis_client():
    return redis_client

def get_cached_data(key: str) -> Optional[str]:
    """ Récupérer une donnée depuis Redis """
    cached_data = redis_client.get(key)
    return cached_data

def cache_data(key: str, value: str, ttl: int = 3600):
    """ Stocker une donnée dans Redis avec un temps d'expiration """
    redis_client.setex(key, ttl, value)

def delete_cache(key: str):
    """ Supprimer une donnée du cache Redis """
    redis_client.delete(key)


    
