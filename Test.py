import random

def spin_the_wheel():
    # 定义奖项和对应的概率
    prizes = {
        "一等奖": 0.1,
        "二等奖": 0.2,
        "三等奖": 0.3,
        "安慰奖": 0.4,
    }

    # 计算总概率
    total_probability = sum(prizes.values())

    # 随机生成一个0到总概率之间的数字
    random_number = random.uniform(0, total_probability)

    # 找到对应的奖项
    for prize, probability in prizes.items():
        if random_number < probability:
            return prize

# 使用示例
print("开始摇奖...")
prize = spin_the_wheel()
print("恭喜您获得了：", prize)