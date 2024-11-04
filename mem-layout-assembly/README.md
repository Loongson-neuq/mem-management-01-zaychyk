# C++ 内存布局的汇编实现

在本题中，你将实践如何将高层次的 C++ 代码翻译成一个简单的伪汇编语言。你需要熟悉栈和堆的内存分配原理，并通过低级指令来实现 C++ 代码中的变量分配和初始化，特别是区别对待栈上和堆上的内存分配。

## 代码示例
以下是给定的 C++ 函数 `func()`：

```cpp
void func() {
    int a = 42;
    int* ptrA = &a;

    int array[512];
    Object* obj = new Object();
    char* str = "Hello"; 
    StructType value = StructType {1, 2, 3}; 
    StructType* pValue = (StructType*)malloc(sizeof(StructType));
    std::vector<int> vec = {1, 2, 3};
}
```

类型的定义详细可以参考课件，不过事实上不需要。

你需要将此代码转换为以下指令集的伪汇编语言。

## 汇编语言指令集

- **PUSH <value>** - 将 `<value>` 压入栈，栈指针 (`SP`) 减少。
- **POP <register>** - 从栈中弹出一个值，存入 `<register>`，栈指针 (`SP`) 增加。
- **LEA <dest>, <src>** - 将 `<src>` 的地址加载到 `<dest>`，用于获取栈上变量的地址。
- **ADD <register>, <imm>** - 将 `<register>` 寄存器增加 `<imm>` 大小，`<imm>` 只能为立即数（但可为负数，仅能在[-4096, 4095] 范围内）
- **HEAP_ALLOC <dest>, <size>** - 从堆上分配 `<size>` 字节的内存，将指针存入 `<dest>`。
- **HEAP_FREE <pointer>** - 释放 `<pointer>` 指向的堆内存。
- **MOV <dest>, <src>** - 将 `<src>` 的值复制到 `<dest>`（可以是寄存器或内存地址）。
- **STORE <address>, <value>** - 将 `<value>` 存储到 `<address>` 指向的内存。
- **LOAD <register>, <address>** - 从 `<address>` 指向的内存加载数据到 `<register>`。

## 任务要求

0. **实现函数的序幕和尾声**：在伪汇编实现中，添加函数的“序幕”和“尾声”部分，确保栈帧的管理正确。具体要求如下：
   - **序幕**：在函数开头将返回地址和当前栈指针等寄存器值压入栈中，完成栈帧的初始化。
   - **尾声**：在函数末尾恢复栈帧，清理栈上的局部变量，确保返回地址正确。
   - 栈顶指针寄存器为为 `SP`，基指针寄存器为 `BP`。

1. **栈上的变量**：`a` 和 `array` 是局部变量，因此应在栈上分配。通过 `PUSH` 指令为每个变量分配空间，例如每个数组元素都用 `PUSH` 单独初始化，以此强调栈上的数组本质上是多个匿名变量。
   
2. **堆上的变量**：使用 `HEAP_ALLOC` 分配 `obj` 和 `pValue`，实现类似于 `new` 或 `malloc` 的堆分配。

3. **结构体的分配和初始化**：
   - 栈上结构体 `value` 的每个字段都使用 `PUSH` 单独初始化，并计算出结构体的基址。
   - 堆上结构体 `pValue` 使用 `HEAP_ALLOC` 分配空间，并使用 `STORE` 指令逐个字段初始化。

4. **字符串常量**：`str` 是指向字符串常量的指针，用 `MOV_STR` 加载字符串到 `str`。

5. **清理栈上的分配**：函数结束时恢复栈指针，回收栈上局部变量的空间。

6. **寄存器**：除`SP` 和 `BP` 之外，你可以不超过 4 个寄存器，分别为 `t0` 到 `t3`。每个寄存器大小为 64 位。你需要在最后恢复你使用过的寄存器。

7 **架构**：要求为 64 位架构，栈和堆的地址空间为 64 位，指针大小为 64 位。

## 任务要求

2. **逐行翻译示例**：每个变量的声明和初始化需要独立实现，并分配在适当的内存区域（栈或堆）。以下是每个变量的要求。

## 变量翻译要求

为以下每个 C++ 变量编写汇编实现示例：

## 1. `int a = 10;`
   - 将整数变量 `a` 初始化为 10，分配在栈上。
   - 示例：实现栈上的整数变量声明和初始化，使用 `PUSH` 指令完成栈分配。

## 2. `int* ptrA = &a;`
   - 定义指针 `ptrA` 并指向变量 `a` 的地址。
   - 示例：使用 `LEA` 指令加载 `a` 的地址到 `ptrA` 中。

## 3. `int array[512];`
   - 在栈上声明一个长度为 512 的整型数组 `array`。
   - 示例：使用 `LEA` 计算数组的起始地址。自己想办法为数组分配空间

## 4. `Object* obj = new Object();`
   - 在堆上分配 `Object` 类型的空间，并将地址赋给指针 `obj`。
   - `Object` 本身不含有任何字段，但是具有三个虚函数`GetHashCode`，`ToString`，`Equals`。
   - 直接在对象上储存 vtable 而不是 pVtable。三个函数的地址分别为 `<Program.exe+Object::GetHashCode>`， `<Program.exe+Object::ToString>`, `<Program.exe+Object::Equals>`
   - 忽略构造函数的调用
   - 示例：使用 `HEAP_ALLOC` 指令完成堆分配，并初始化指针。

## 5. `char* str = "Hello";`
   - 将字符串常量 `"Hello"` 的首地址赋给指针 `str`。
   - 你可以假设字符串常量 `"Hello"` 在程序 elf 的某一位置，你可以通过 `<Program.exe>` 获取到程序在内存中的起始地址，该字符串的偏移你可以任意假定。

## 6. `StructType value = StructType {1, 2, 3};`
   - 声明一个 `StructType` 结构体 `value`，初始化字段 `field1 = 1`，`field2 = 2`，`field3 = 3`。
   - `StructType` 的三个字段均为 `int32`
   - 示例：在栈上逐一声明和初始化字段，并计算结构体的起始地址。

## 7. `StructType* pValue = (StructType*)malloc(sizeof(StructType));`
   - 使用堆分配空间并初始化 `pValue` 指针。
   - 示例：使用 `HEAP_ALLOC` 完成分配，并为 `field1`、`field2`、`field3` 赋值。

## 8. `std::vector<int> vec = {1, 2, 3};`
   - 在堆上分配一个整数向量 `vec`，并初始化元素为 `{1, 2, 3}`。
   - 示例：使用 `HEAP_ALLOC` 分配向量的空间，并逐个初始化元素值。

---

# 提示

- **栈上的变量**：局部变量在栈上分配，例如 `a` 和 `array`。栈分配通过栈指针操作来实现。
- **堆上的变量**：使用 `HEAP_ALLOC` 实现类似 `malloc` 的堆分配机制，例如 `obj` 和 `pValue`。
- **函数序幕和尾声**：确保函数执行前后栈帧完整和正确。

# 提交内容

请提交一份完整的伪汇编代码，严格按照指令集的定义和任务要求实现 C++ 代码中的内存分配和初始化。

请在每一行给出必要的注释
将你的代码保存在该文件夹的 `func.asm` 内。
