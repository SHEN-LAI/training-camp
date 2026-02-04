# 情报解密
# 截获一条杂乱情报：" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;
# Mission:2025-RESCUE-X "
# 请运用所有所学知识清洗数据：利用 String 方法去除干扰空格；利用 Set 帮特工去除重复装
# 备；利用 Slicing 截取核心任务代号；利用 Tuple锁定坐标；最后将所有信息归档进一个 Dict
# 档案中

#去除空格+拆分操作
Original_intelligence=' Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X '
Original_intelligence=Original_intelligence.strip()
Original_intelligence=Original_intelligence.replace(' ','')
intelligence_list=Original_intelligence.split(';')
print(intelligence_list)

#提取特工代号操作
agent=intelligence_list[0].split(':')[1]
print(agent)

#锁定坐标操作
coords_num=intelligence_list[1].split(':')[1]
x,y=coords_num[1:-1:1].split(',')
x=int(x)
y=int(y)
coords=(x,y)
print(coords)
print(type(coords))

#截取核心任务代号操作
misson=intelligence_list[3].split(':')[1]
print(misson)

#去除重复装备操作
items=set(intelligence_list[2].split(':')[1].split(':'))
print(items)

#利用字典整合
intelligence={'Agent':agent,'Coords':coords,'Items':items,'Mission':misson}
print(intelligence)