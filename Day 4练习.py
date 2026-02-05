#Day 4


#练习一：平方数列表

squares=[i**2 for i in range(1,11)]#一行代码
print(squares)#测试用


#练习二：给全班同学的名字加上统一前缀（用AI生成一组数据）

names = [
    "张明", "李华", "王伟", "刘芳", "陈静",
    "杨帆", "赵强", "周婷", "吴磊", "郑秀",
    "孙悦", "马超", "朱琳", "胡军", "林雪",
    "何勇", "高洁", "罗斌", "梁宇", "宋佳",
    "谢娜", "唐嫣", "韩梅", "冯程", "于娜",
    "董洁", "徐亮", "沈冰", "曾志", "苏晴"
]
new_names=map(lambda x:'QG_'+x,names)
print(list(new_names))


#练习三：能源核心数据清洗(采用新学习函数式编程知识,其中阈值改为0.5）

raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]

def number_judgment(s):
    try:
        float(str(s).strip())
        return True
    except ValueError:
        return False

def list_number_judging(s_list):
    new_list=[]
    for item in s_list:
        if number_judgment(item):
            new_list.append(int(item))
    print(f"数字列表{new_list}")
    return new_list

def output_judgment(s_list):
    new_list=[]
    for i in list_number_judging(s_list):
        if i>=80:
            new_list.append(i)

    #归一化公式：x' = (x - min) / (max - min)处理数据
    list_max=max(new_list)
    list_min=min(new_list)
    to_one_list=map(lambda x:(x-list_min) / (list_max-list_min),new_list)
    to_one_list=list(to_one_list)

    #判断输出
    for item in to_one_list:
        if item >0.5:
            print(f"归一化后数据{item:.2f}核心过载")
        else:
            print(f"归一化后数据{item:.2f}运转正常")

#运行函数
output_judgment(raw_data )