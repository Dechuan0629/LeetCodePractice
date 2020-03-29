import threading
import sys

class TypeError(Exception):
    def __init__(self):
        print("TypeError:",end="")

def printNumber(n):              #仿造的leetcode上对printnumber奇偶数的异常判断
    FuncName = sys._getframe().f_back.f_code.co_name
    LineNumber = sys._getframe().f_back.f_lineno
    try:
        if FuncName == 'zero':
            if n != 0:
                raise TypeError()
        elif FuncName == 'even':
            if n % 2 != 0:
                raise TypeError()
        elif FuncName == 'odd':
            if (n + 1) % 2 != 0:
                raise TypeError()
    except TypeError:
        print("line",LineNumber)
        print("You passed invalid value.(",n,")is not",FuncName,",Exiting!")
        exit(-1)
    else:
        print(n)

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_zero = threading.Lock()
        self.lock_even = threading.Lock()
        self.lock_odd = threading.Lock()
        self.lock_even.acquire()         #因为是先输出0，所以在构造时先对奇偶数输出加锁
        self.lock_odd.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.lock_zero.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.lock_odd.release()  #从i=0开始会输出010，从1开始交替输出，需要输出哪种数时，对那个数解锁，当那个数输出完成后，对0解锁
            else:
                self.lock_even.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.lock_even.acquire()
            printNumber(i)
            self.lock_zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.lock_odd.acquire()
            printNumber(i)
            self.lock_zero.release()



def main():
    n = input("input a number:")
    n = int(n)
    test = ZeroEvenOdd(int(n))
    t1 = threading.Thread(target=test.zero,args=(printNumber,))
    t2 = threading.Thread(target=test.odd,args=(printNumber,))
    t3 = threading.Thread(target=test.even,args=(printNumber,))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main()