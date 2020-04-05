import time
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0
        self.cache = {}

    def get(self, key: int) -> int:
        try:
            ans = self.cache[str(key)][0]
            self.cache[str(key)][1]+=1
            self.cache[str(key)][2] = round(time.time() * 1000000)
        except KeyError:
            return -1
        else:
            return ans

    def put(self, key: int, value: int) -> None:         #本可以一次ac，没考虑到put相同的key时，也会占用操作次数
        try:
            if self.current_capacity < self.capacity:    #每一个键值对保存的形式为key：[value，次数，时间戳]
                if str(key) in self.cache:
                    self.cache[str(key)][0] = value
                    self.cache[str(key)][1] += 1
                    self.cache[str(key)][2] = round(time.time() * 1000000)   #时间戳精准到微秒
                else:
                    self.cache.update({str(key):[value,0,round(time.time() * 1000000)]})
                    self.current_capacity+=1
            else:
                if str(key) in self.cache:
                    self.cache[str(key)][0] = value
                    self.cache[str(key)][1] += 1
                    self.cache[str(key)][2] = round(time.time() * 1000000)
                else:
                    key_min = min(self.cache.keys(), key=(lambda k: self.cache[k][1:]))  #利用min函数找出次数最少的，优先级为 操作次数 > 操作时间
                    del self.cache[key_min]                                              #如果次数相同，会按照时间戳判断，时间戳小的，说明最近没有使用，因此会删除
                    self.cache.update({str(key): [value, 0, round(time.time() * 1000000)]})
        except ValueError:
            return -1


def main():
    capacity = input('input the cache capacity:')
    cache = LFUCache(int(capacity))
    cache.put(2,1)
    cache.put(2,2)
    cache.get(2)
    while True:
        op = input('input operator:')
        if op == 'put':
            key,value = map(int,input('input key,value:').split(','))
            cache.put(key,value)
        elif op == 'get':
            key = input('input key:')
            print(cache.get(int(key)))
        else:
            break

if __name__ == '__main__':
    main()