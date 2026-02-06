#练习一
#该练习结合AI一步步理解完善，部分代码由AI生成后已理解，并加以完善

class Shape:
    #图形基类
    # 类变量：记录所有图形创建数量
    _total_shapes = 0

    def __init__(self):
        self.__area = None
        self._dimensions = {}
        Shape._total_shapes += 1
        self._id = Shape._total_shapes

    def _calc_area(self):
        print("子类需重写此方法")

    def get_area(self):
        if self.__area is None:
            self.__area = self._calc_area()
        return self.__area

    @classmethod#类方法而不是实例方法
    def get_total_count(cls):
        return cls._total_shapes


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        # 存储尺寸
        self._dimensions['radius'] = radius

    def _calc_area(self):
        import math
        radius = self._dimensions['radius']
        return math.pi * radius * radius


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        # 存储尺寸
        self._dimensions['width'] = width
        self._dimensions['height'] = height

    def _calc_area(self):
        width = self._dimensions['width']
        height = self._dimensions['height']


# 测试代码
if __name__ == "__main__":
    circle = Circle(5.0)
    print(f"圆形面积: {circle.get_area():.2f}")  # 通过公开方法获取

    rect = Rectangle(4.0, 6.0)
    print(f"矩形面积: {rect.get_area()}")

    # 获取总数
    print(f"图形总数: {Shape.get_total_count()}")

    # 尝试直接访问私有属性会失败
    try:
        print(circle.__area)  # AttributeError
    except AttributeError:
        print("无法直接访问私有属性 __area")

    # 多态
    shapes = [circle, rect]
    for shape in shapes:
        print(f"面积: {shape.get_area()}")


#练习二
#结论：str.strip()默认移除字符串两端的所有空白字符（包括空格、制表符、换行符等），而不仅仅是空格字符

# 测试 str.strip() 的默认行为
test_strings = [
    "  Hello World  ",      # 普通空格
    "\tHello World\t",      # 制表符
    "\nHello World\n",      # 换行符
    "  \t\nHello World\n\t  ",  # 混合空白字符
    "Hello World",          # 无空白字符
]

print("测试 str.strip() 默认行为:")
for s in test_strings:
    result = s.strip()
    print(f"strip({repr(s)}) = {repr(result)}")

# strip('  Hello World  ') = 'Hello World'
# strip('\tHello World\t') = 'Hello World'
# strip('\nHello World\n') = 'Hello World'
# strip('  \t\nHello World\n\t  ') = 'Hello World'
# strip('Hello World') = 'Hello World'