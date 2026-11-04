# API 参考

`calculator` 模块只提供两个纯函数，用于演示单元测试的自动化执行。

## `add(a, b)`

返回两个数的和。

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `a` | `int` / `float` | 加数 |
| `b` | `int` / `float` | 加数 |
| 返回值 | `int` / `float` | `a + b` |

示例：

```python
>>> from calculator import add
>>> add(2, 3)
5
>>> add(-1, 1)
0
```

## `multiply(a, b)`

返回两个数的积。

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `a` | `int` / `float` | 乘数 |
| `b` | `int` / `float` | 乘数 |
| 返回值 | `int` / `float` | `a * b` |

示例：

```python
>>> from calculator import multiply
>>> multiply(3, 4)
12
>>> multiply(2, 0)
0
```

## 测试用例覆盖情况

| 用例 | 断言 |
| --- | --- |
| `test_add` | `add(2, 3) == 5`、`add(-1, 1) == 0`、`add(0, 0) == 0` |
| `test_multiply` | `multiply(3, 4) == 12`、`multiply(2, 0) == 0`、`multiply(-2, 3) == -6` |
