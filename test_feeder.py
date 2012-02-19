
import redis
import time

if __name__ == '__main__':
    r = redis.Redis(unix_socket_path='/home/salvarez/apps/redis/redis.sock')
    
    t = time.time()
    for n in range(1000):
        r.lpush("pycola:1", "http://localhost/?n=%i" % n)
        #open('/home/salvarez/tmp/pycolatest/%i' % n, 'w').write("http://localhost/?n= %i" % n)

    print "%fsecs" % ((time.time() - t))