# -*- coding: utf-8 -*-
# 猜数字小游戏：电脑随机想一个 1~100 的整数，玩家来猜
# 运行方式：python guess_number.py

import random
import sys


def safe_input(tip):
    # 正常读一行；如果输入被中断（比如管道输入结束），就当成退出游戏
    try:
        return input(tip)
    except EOFError:
        print("\n输入结束，游戏退出，再见！")
        sys.exit(0)


def main():
    print("=" * 34)
    print("        猜 数 字 小 游 戏")
    print("     范围：1 ~ 100")
    print("=" * 34)

    while True:
        # 电脑随机生成一个 1~100 的答案
        answer = random.randint(1, 100)
        count = 0  # 记录猜了几次

        print("\n我已经想好了一个 1~100 的数字，来猜猜看！")
        print("（输入 0 可以直接认输）")

        while True:
            s = safe_input("请输入你猜的数字：")

            # 判断输入是不是合法数字
            if not s.lstrip("-").isdigit():
                print("  → 请输入一个正整数！")
                continue

            guess = int(s)
            count += 1

            if guess == 0:
                print("  你选择了认输，答案是 %d。" % answer)
                break
            elif guess < 1 or guess > 100:
                print("  → 超出范围啦，只能猜 1~100！")
                count -= 1  # 无效输入不算次数
            elif guess < answer:
                print("  小了！再大一点。")
            elif guess > answer:
                print("  大了！再小一点。")
            else:
                print("  ★ 恭喜你，猜对了！答案就是 %d。" % answer)
                print("  你一共猜了 %d 次。" % count)
                if count <= 5:
                    print("  太厉害了，简直是天才！")
                elif count <= 7:
                    print("  不错嘛，很聪明！")
                else:
                    print("  再接再厉，下次可以更少次哦！")
                break

        # 询问是否再来一局
        again = safe_input("\n再来一局？(y/n)：").strip().lower()
        if again != "y":
            print("游戏结束，再见！")
            break


if __name__ == "__main__":
    main()
