# 探索调用栈

给定已有的代码：

```c
#include <stdio.h>

void inner_function() {
   // 在栈上分配的局部变量
   char buffer[16];
    
   printf("Your input will be stored at: %p\n", (void*)buffer);
   printf("Current function's rbp is at: %p\n", (void*)__builtin_frame_address(0));
    
   puts("Enter something:");
   gets(buffer);  // 故意使用不安全的gets
}

void middle_function() {
   puts("Now in middle_function");
   printf("Middle function's rbp is at: %p\n", (void*)__builtin_frame_address(0));
   inner_function();
   puts("This line should not be executed!");
}

void target_function() {
   puts("Congratulations! You've successfully modified the return address!");

   exit(0);
}

int main() {
   printf("Main function's rbp is at: %p\n", (void*)__builtin_frame_address(0));
   middle_function();

   printf("Sorry, you didn't successfully hacked the return address");
   return 1;
}
```

该代码中存在以下调用链：

```
main -> middle_function -> inner_function
```

你需要在**不修改**代码的情况下，使得控制流变为：

```
main -> middle_function -> inner_function 
        然后middle_function返回时跳转到 target_function
        (而不是返回到main)
```

## 控制流过程中栈的结构

```
高地址
+------------------------+
|     main的栈帧         |
+------------------------+
| middle_function返回地址 | <-- 这是你要修改的目标(rbp-8)
| 保存的main的rbp       | <-- middle_function的rbp指向这里
+------------------------+
| inner_function返回地址  |
| 保存的middle的rbp      | <-- inner_function的rbp指向这里
+------------------------+
|        buffer         | <-- 输入存储的位置
+------------------------+
低地址
```

## 实验步骤：
1. 首先使用`gcc -g -fno-stack-protector program.c -o program`编译程序。

2. 使用gdb分析栈的结构：
```bash
gdb ./program
b inner_function
r
```

3. 在 gdb 中观察栈的布局：
```gdb
(gdb) x/xg $rbp        # 查看当前函数保存的rbp
(gdb) x/xg ($rbp)      # 查看middle_function的rbp
(gdb) x/xg ($rbp+8)    # 查看当前函数的返回地址
(gdb) x/xg *($rbp)-8   # 查看middle_function的返回地址
```

你的任务：
1. 分析程序中三个栈帧的关系：
   - main的栈帧
   - middle_function的栈帧
   - inner_function的栈帧

2. 目标：从inner_function中修改middle_function的返回地址
   - 首先找到inner_function的rbp
   - 通过inner_function的rbp找到middle_function的rbp
   - 计算middle_function返回地址的位置（rbp-8）
   - 构造输入使程序跳转到target_function

详细实验过程：
1. 使用`objdump -d program`找到target_function的地址

2. 计算需要的偏移量：
   - 从buffer到inner_function的rbp有多远？
   - 从inner_function的rbp到middle_function的rbp有多远？
   - 从middle_function的rbp到它的返回地址有多远？

3. 构造payload：
   ```python
   #!/usr/bin/env python3
   padding = b'A' * offset_to_saved_rbp
   new_return_addr = target_function_addr.to_bytes(8, 'little')
   payload = padding + new_return_addr
   print(payload)
   ```

## 注意事项：
1. 程序中输出了关键地址，可以帮助你理解内存布局
2. x86_64使用小端序
3. 地址是8字节对齐的

## 要求：
1. 编写你对栈帧结构的理解（30分）
2. 正确计算偏移量（30分）
3. 成功构造 payload（20分）

实验结果请附上详细步骤，包括编写的代码，以及实验过程的截图。

将所有结果储存在 `Solution.md` 中

## 补充基础知识

1. 什么是栈？
   - 栈是程序运行时的一块内存区域
   - 特点是"后进先出"(LIFO)
   - 在x86_64系统中，栈从高地址向低地址增长
   - 主要用于存储：
     * 函数的局部变量
     * 函数调用时的参数
     * 返回地址
     * 保存的寄存器值

2. 什么是栈帧？
   - 每个函数调用都会创建一个栈帧
   - 栈帧包含了函数运行所需的所有信息
   - 使用rbp（基址指针）和rsp（栈指针）来管理

3. 栈帧的结构（从高地址到低地址）：
```ascii
高地址
             上一个函数的栈帧
          +------------------+
          |  参数 6         |  如果有第6个及以上的参数
          |  参数 7         |
          |  ...           |
rbp+16 -> |  参数 5         |
rbp+8 ->  |  返回地址       |  <- 这是我们要修改的目标
rbp ----> |  保存的老rbp    |  <- 指向上一个函数的rbp
rbp-8 ->  |  局部变量1      |
          |  局部变量2      |
          |  ...           |
rsp ----> |  栈顶          |
低地址
```

4. 函数调用过程：
```nasm
; 调用函数前：
push rbp          ; 保存当前的rbp
mov rbp, rsp      ; 设置新的rbp
sub rsp, N        ; 为局部变量分配空间

; 函数返回时：
mov rsp, rbp      ; 恢复栈指针
pop rbp           ; 恢复上一个函数的rbp
ret               ; 返回（从栈上弹出返回地址并跳转）
```

### gdb 使用技巧

基础调试命令：
```bash
# 启动程序调试
gdb ./program # 把 ./program 换成实际的可执行文件

# ===========
# 进入 gdb 后
# ===========

# 设置断点
b inner_function     # 在inner_function函数开始处设置断点
b *0x4011ab         # 在特定地址设置断点，不建议是死于

# 运行程序
r                   # 运行程序直到断点
n                   # 单步执行，跳过函数调用
s                   # 单步执行，会进入函数内部
c                   # 继续运行直到下一个断点

# 查看程序状态
i r                 # 查看所有寄存器的值
i r rbp             # 只查看rbp寄存器的值
i r rsp             # 只查看rsp寄存器的值

# 开启反汇编界面
layout asm          # 开启反汇编界面
```

查看内存内容：
```bash
# 查看栈内存
x/16gx $rsp         # 从栈顶开始，显示16个8字节的内存内容
x/16gx $rbp         # 从rbp开始，显示16个8字节的内存内容
x/s 地址            # 将内存内容作为字符串显示
x/i 地址            # 将内存内容作为指令显示

# 查看特定地址的内存
x/gx $rbp           # 查看保存的上一个函数的rbp
x/gx $rbp+8         # 查看返回地址
x/gx *($rbp)        # 查看上一层函数的rbp的内容
x/gx *($rbp)-8      # 查看上一层函数的返回地址
```

获取重要信息：
```bash
# 查看函数地址
p target_function   # 打印target_function的地址

# 查看变量地址
p &buffer           # 打印buffer的地址
p/x $rbp           # 以十六进制打印rbp的值

# 查看栈帧信息
info frame          # 显示当前栈帧的详细信息
bt                  # 显示函数调用栈（backtrace）
```

其他有用的命令：
```bash
# 设置显示格式
set print pretty on    # 让结构体显示更易读
set disassembly-flavor intel  # 使用intel汇编语法

# 反汇编
disas inner_function   # 反汇编inner_function函数
disas                 # 反汇编当前函数

# 在运行时修改内存（用于测试）
set {int}0x12345678 = 0x90909090   # 修改特定地址的内存值
```

实验技巧：
1. 使用断点时机：

```bash
# 在gets函数之前设置断点，记录初始状态
b gets
r
# 记录关键地址
p $rbp
p &buffer
```

2. 观察栈的变化：
```bash
# 在输入前后观察栈的内容变化
x/32gx $rsp  # 输入前记录
c            # 继续执行
x/32gx $rsp  # 输入后比较
```

3. 确认payload效果：
```bash
# 在ret指令处设置断点
disas inner_function    # 找到ret指令的地址
b *0x401234            # 在ret处设置断点
# 运行到ret前，确认栈上的返回地址已被修改
x/gx $rsp
```

调试建议：
1. 先用小输入测试程序正常运行流程
2. 使用断点确认buffer和rbp的具体位置
3. 在构造payload前，仔细记录所有关键地址
4. 通过gdb确认payload正确覆盖了目标位置
