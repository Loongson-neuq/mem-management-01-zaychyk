# 双向链表实现

## **语言**：C

## **问题**：
1. 实现一个双向链表结构，包含插入和删除操作。链表的定义如下：

    ```c
    typedef struct LinkedList LinkedList;

    struct LinkedList {
        // ???
    };
    ```

2. 链表节点的定义如下：
   ```c
   typedef struct Node {
       // ???
   } Node;
   ```

2. 编写 `void insert_head(LinkedList*, Node*)` 函数，将一个新节点插入到链表的头部。
3. 编写 `void insert_tail(LinkedList*, Node*)` 函数，将一个新节点插入到链表的头部。
4. 编写 `Node* get_nth_node(LinkedList*, int)` 函数，获取链表中的第 `n` 个节点。没有就返回 `NULL`
5. 编写 `BOOL delete_node(Node*)` 函数，通过获取到的节点删除链表内部的节点。
6. 编写 `void free_list(LinkedList*)` 函数，根据数据值删除链表中的节点。
7. 为链表和节点类型定义工厂函数 `LinkedList* create_list()` 和 `Node* create_node()`。

## **提示**：

1. `BOOL` 是 `int` 的别名，定义如下：

```c
#define BOOL int
```

2. 使用 `malloc_mocked` 和 `mock_free_mocked` 函数模拟内存分配和释放。

不要使用 `malloc` 和 `free` 函数，使用了也会被测试框架拦截。

3. 不需要处理可能存在的*环*问题。

4. 上面说的 `malloc_mocked`, `free_mocked` 和 `BOOL` 已经在 `test_essential.h` 中定义，不要再定义了。

## **要求**：

1. 实现内存管理，确保在删除节点时释放内存，防止内存泄漏。同时确保内存安全

2. 储存代码在 `LinkedList.h` 文件中。

3. 如果需要测试，请自己在 `main.c` 中编写测试代码引用 `LinkedList.h`
