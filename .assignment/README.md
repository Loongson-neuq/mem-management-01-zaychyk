本文件夹用于储存标识作业元信息的文件及作业提交器。

**对于作业的说明以及其他附加信息请放在仓库根目录的 `README.md` 中而不是本文件中。**

## 文件结构
```
- config.json - 作业配置文件
- Submitter/ - 作业提交器代码
```

对于以上文件的详细说明位于[Loongson-neuq/LoongsonNeuq](https://github.com/Loongson-neuq/LoongsonNeuq)，下文只提供简要说明。

## config.json

作业配置文件，用于标识作业的元信息。**每次布置新作业时需要更新该文件。**
请注意格式的正确性，因此请仔细阅读以下说明。
可以使用 `check_config.py` 脚本进行格式检查。

## Submitter

~~用 C# 编写的作业提交器，用于提交作业。学生无需手动运行，在 commit 到 GitHub 时会在 GitHub Actions 中自动运行。请注意查看 GitHub Actions 的输出，以确认提交是否成功。通常如果没有报错，提交就是成功的。~~

已迁移至 [Loongson-neuq/LoongsonNeuq](https://github.com/Loongson-neuq/LoongsonNeuq)
