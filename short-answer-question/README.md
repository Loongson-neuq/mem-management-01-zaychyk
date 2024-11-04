# 简答题

## 要求

在每道题目后面的代码块里填写你的答案。

### 题目

#### 1. 理解变量分配的题目

1.1 在以下代码中，指出每个变量（包括指针、对象和结构体）分配的位置（堆/栈）：
   
```cpp
void func() {
    int a = 10;
    int* ptrA = &a;
    int* ptrB = new int(20);
    std::string str = "Hello";
    std::vector<int> vec = {1, 2, 3};
}
```

- Stack

栈上分配了哪些对象，分别占用多少内存？

你的答案：

```ascii

```

- Heap

堆上分配了哪些对象，分别占用多少内存？（不考虑对象头，虚函数表指针等）

你的答案：

```ascii

```

1.2 为什么`ptrA`和`str`变量本身在栈上分配，而它们指向的内存不一定在栈上？

你的答案：

```ascii

```

1.3 编写一小段代码，测量 `vec1` 和 `vec2` 的内存占用，并说明为什么存在这种区别

```cpp
std::vector<int> vec1;
std::vector<int>* vec2 = new std::vector<int>();
```

你的答案：

```cpp

```

说明：

```ascii

```

#### 2. 堆内存和垃圾回收的题目

2.1 当程序在堆上分配内存时，为什么需要调用 `free` 或 `delete` 释放该内存？如果不释放会发生什么问题？

你的答案：

```ascii

```

2.2 简述 `malloc` 和 `new` 的不同之处，如何选择它们？

你的答案：

```ascii

```

#### 3. 虚拟内存和系统调用的题目

3.1 在类 Unix 系统中，`malloc` 是如何调用 `brk` 或 `sbrk` 系统调用来给标准库分配内存的？

你的答案：

```ascii

```

3.2 尝试使用 `brk` 或 `sbrk` 分配 1024 字节，并尝试访问第 1024 ~ 4095 字节的内存，说明为什么可以访问这些内存？

你的答案：

```ascii

```

附上你完成这个操作的代码和截图：

```

```

#### 4. 栈与堆的性能比较

4.1 为什么通常认为栈的访问速度比堆快？解释栈和堆在指令访问方式上的差异。

你的答案：

```ascii

```

4.2 为什么栈内存的分配必须是固定大小的，而堆内存可以动态调整？

你的答案：

```ascii

```

#### 5. 栈帧和调用栈的题目

5.1 简述函数调用时栈帧的创建过程，并解释栈帧的作用。

你的答案：

```ascii

```

5.2 为什么异常抛出时会生成栈追踪（Stack Trace）？栈追踪信息中显示的函数调用顺序有什么特点？

你的答案：

```ascii

```

5.3 根据以下栈追踪信息，解释程序中可能的调用链，并指出在哪个函数中抛出了异常：

```ascii
Unhandled exception. System.Exception: Exception from FunctionC
   at Program.FunctionC() in Program.cs:line 24
   at Program.FunctionB() in Program.cs:line 17
   at Program.FunctionA() in Program.cs:line 11
   at Program.Main(String[] args) in Program.cs:line 5
```

你的答案：

```ascii

```

#### 6. 结构体和类的分配对比

6.1 为什么结构体通常被分配在栈上，而类实例通常分配在堆上？这种分配上的差异如何影响它们的使用？

你的答案：

```ascii

```

6.2 为什么 C++ 允许将类实例分配在栈上？试举例说明如何在栈上创建类实例

你的答案：

```ascii

```

6.3 编写一段代码，展示栈上分配类实例会损失什么重要的特性。

```C++

```
