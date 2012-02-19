
import pycola2
import redis_loader

if __name__ == '__main__':
    run = pycola2.Pycola(100, redis_loader.RedisLoader)
    run.loop()
