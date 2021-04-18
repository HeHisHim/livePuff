### [线程的竞争条件](https://blog.csdn.net/hzrandd/article/details/53883728, https://zhuanlan.zhihu.com/p/33158981)

## **`竞争条件`**
竞争条件(race condition)也叫竞态条件, 它旨在描述一个系统或进程的输出依赖于不受控制的事件出现顺序或者出现时机. 该词源自于两个信号试着彼此竞争来影响谁先输出. 举例来说, 如果两个线程同时试图修改同一个共享的变量, 在没有并发控制的情况下, 最后的结果依赖于两个线程的执行顺序和时机. 如果发生了并发访问冲突, 则最后的结果是不正确的

## **`如两个线程对b=5进行+=1的计算`**
## **`理想中的执行顺序`**
* (thread1) load b into some register in thread 1
* (thread1) add 1 to thread 1's register, computing 6
* (thread1) store the register value (6) to b
* (thread2) load b into some register in thread 2
* (thread2) add 1 to thread 2's register, computing 7
* (thread2) store the register value (7) to b
## **`非理想中的执行顺序`**
* (thread1) load b into some register in thread 1
* (thread2) load b into some register in thread 2
* (thread1) add 1 to thread 1's register, computing 6
* (thread2) add 1 to thread 2's register, computing 6
* (thread1) store the register value (6) to b
* (thread2) store the register value (6) to b
### 初始值b为5, 两个线程对其计算+1, 最终结果可能为6. 这是因为两个线程互相干扰, 从而导致产生错误的计算结果. 通常, 线程不是以原子的方式执行的. 另一个线程可以在任何两个指令期间打断它, 而且还可以使用共享的资源. 如果一个安全的程序没有预防这些中断, 那么另一个线程就会干扰执行顺序. 在一个安全程序中, 不管任何指令之间运行了多少其他线程, 都应该保证其正确性. 关键是当程序访问某一资源时, 需保证其他线程无法对该资源进行干扰

## **`解决竞争条件`**
* 一般是对共享资源加锁


