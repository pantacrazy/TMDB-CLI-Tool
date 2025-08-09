import json
class StoreConst:
    def __init__(self,server=None,port=None):
        self._store_cache = None
        self.names={'cache':'cache.json'}
    def set_store_cache(self,cache=None):
        if cache is not None and not self.is_cache_in(cache):
            if self._store_cache is None:
                self._store_cache=[]
            self._store_cache.append(cache)
            
            json.dump(self._store_cache,open(self.names.get('cache'),'w'),indent=2)
        else:
            json.dump(self._store_cache,open(self.names.get('cache'),'w'),indent=2)
    def get_store_cache(self):
            try:
                self._store_cache=json.load(open(self.names.get('cache')))
            except:
                self.set_store_cache()
            return self._store_cache
    def is_cache_in(self,cache):
        actual_cache=self.get_store_cache()
        if actual_cache is None:
            open(self.names.get('cache'),'w',encoding='utf-8')
        else:
            self._store_cache=actual_cache
        if self._store_cache is None:
            return False
        else:  return cache in self._store_cache
    def clear_cache(self):
        self._store_cache=None
        self.set_store_cache(None)