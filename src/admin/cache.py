from admin.settings import redis_cli

redis_cli = redis_cli()


class ApiSession:
    EXPIRES_AT = 15

    @staticmethod
    def set(key, value):
        redis_cli.set(key, value)

    @staticmethod
    def get(key):
        return redis_cli.get(key)

    @classmethod
    def refresh(cls, key):
        access_key = cls.get(key)
        if access_key:
            pass
