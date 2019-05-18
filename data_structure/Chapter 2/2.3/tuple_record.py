# 把元组用作记录

lax_coordinates = (33.924, -118.10)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 元组拆包
traveler_id = [('USA', '312315'), ('BRA', 'CE2316131'), ('ESP', 'XD1315331')]

for passport in sorted(traveler_id):    
    print('%s/%s' % passport)     # 元组拆包

# _ 占位符
# for循环提取元组中的元素,也叫做拆包
for country, _ in traveler_id:
    print(country)

a = 4
b = 5

b, a = a, b
print(a, b)



