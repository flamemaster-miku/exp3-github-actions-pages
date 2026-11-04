"""一个用于演示 GitHub Actions 自动化测试的简单计算器模块。"""


def add(a, b):
    """返回两个数的和。"""
    return a + b


def multiply(a, b):
    """返回两个数的积。"""
    return a * b


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("multiply(3, 4) =", multiply(3, 4))
