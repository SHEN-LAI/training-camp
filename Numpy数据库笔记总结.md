## Numpy数据库笔记总结

- Numpy的数据对象nparray形式与相似，但实际上是两种数据结构，特点是存储单一数据类型、连续内存、高效向量化操作

- ### 广播机制

  - 

    **规则1**：维度不同，在较小数组前补1

  - 

    **规则2**：形状不匹配，维度为1的扩展

  - 

    **规则3**：所有维度匹配或为1

    

  - 不满足广播规则时报错，并且要注意维度自动扩展方向

- 需要设置随机种子使结果**可复现**，这点经常被忽略

- Numpy中经常使用`np.where(condition, x, y)`替代if-else

### 常用函数

np.abs(arr)        # 绝对值
np.sqrt(arr)       # 平方根
np.exp(arr)        # 指数
np.log(arr)        # 自然对数
np.sin(arr)        # 三角函数
np.add(arr1, arr2) # 加法
np.multiply(a,b)   # 乘法
np.dot(a,b)        # 点积



