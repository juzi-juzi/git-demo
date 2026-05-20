IS_NARCISSUS_TEXT = "是水仙花数"
IS_NOT_NARCISSUS_TEXT = "不是水仙花数"


def is_narcissus_number(number: int) -> bool:
    """判断一个整数是否为三位水仙花数。"""

    # 水仙花数这里只按三位数定义处理，范围外直接返回 False。
    if number < 100 or number > 999:
        return False

    # 用 divmod 依次拆出百位、十位和个位，再按定义比较立方和。
    hundreds, remainder = divmod(number, 100)
    tens, ones = divmod(remainder, 10)
    return hundreds ** 3 + tens ** 3 + ones ** 3 == number


def main() -> None:
    """读取输入并输出水仙花数判断结果。"""

    number = int(input())
    # 根据判断结果输出对应提示。
    print(IS_NARCISSUS_TEXT if is_narcissus_number(number) else IS_NOT_NARCISSUS_TEXT)


if __name__ == "__main__":
    main()
