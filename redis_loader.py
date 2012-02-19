
import redis



class RedisLoader(object):

    def __init__(self):
        self.r = redis.Redis(unix_socket_path='/home/salvarez/apps/redis/redis.sock')

    def load(self):
        tmp = self.r.lrange('pycola:1', 0, 999)
        self.r.ltrim('pycola:1', 0, ((len(tmp)+1)*(-1)))
        return tmp
