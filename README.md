# 第三周至第六周作业

由于助教们也要考试，第四周和第五周无法上课，所以第三周至第六周的作业一起布置。

内容可能较多，但时间较长，所以请大家尽早开始。

内容主要涉及到课程内容的复习和深入，更多的则是要求大家进行实验和探索。

大家做实验时不要追求速度，要追求深度，要追求对实验结果的理解。

## 作业一

[课件](https://loongson-neuq.pages.dev/p/advanced-rust/)

[上次作业讲解](https://loongson-neuq.pages.dev/p/os-week2-%E4%BD%9C%E4%B8%9A%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98/)

本仓库下有数个文件夹，每个文件夹对应一个实验题目，大家需要完成这些实验。

## Rust & Rustlings

大家别忘了 Rust 和 Rustlings。

### Rust

自学 [Rust Book](https://rust-book.cs.brown.edu/) 第 5, 6 章节，并完成里面的所有 Quizzes。

预习第 4 章节。

#### Rust 猜数游戏

阅读我提供的代码[版本](https://github.com/Loongson-neuq/rust-basic-01-Cai1Hsu/tree/master/guess_game)，重构你的代码。

确保你的代码能够通过 `cargo clippy` 和 `cargo fmt`。

修改你的代码，实现 0 堆分配，即 不使用 `String` 以及其他智能指针。

将新的代码提交在本仓库下，并在 `main.rs` 中用注释写下你的思考。

### Rustlings

修改上次的作业以满足 clippy 和 rustfmt 的要求。

完成 `structs`, `enums`, `strings`, `options`, `clippy`, `quiz2` 这几个章节。不要动没有提到的章节，尤其是 `move_semantics`。

在练习时，在终端中运行 `rustligns watch` 可以实时查看当前题目完成情况，在终端中运行一遍 `rustlings lsp`， 然后重启编辑器可以开启智能提示（你需要提前配置rustling环境和vscode环境）。

点击这个链接接受作业：https://classroom.github.com/a/OkMvYA1o

#### 注意：
##### 提交后在commit的评论或者 `grading-result` 分支上查看评测结果
##### 本地通过了的题目在远程不一定会通过，还会进行 Clippy 和 format 检查
##### 可以点击每题对应的 `stdout.txt` 查看每题的评测结果
##### 评测过程需要大约两分钟，可以在仓库的 `Actions` 页面查看 CI 评测的过程