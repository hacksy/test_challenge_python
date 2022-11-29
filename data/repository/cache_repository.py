from functools import lru_cache


class CacheRepository:

    @lru_cache(maxsize=32)
    def get(self, id: str, status: int):
        """ Cached Custom property that sets the active or inactive status"""
        print("Called")
        return 'Active' if status else 'Inactive'
