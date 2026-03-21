import json
import numpy as np
import math


class VectorOps:

    def __init__(self, axes):
        self.axes = np.array(axes)

    def get_coords(self, vec):
        """获取坐标"""
        A = self.axes.T
        return np.linalg.solve(A, vec)

    def change_axis(self, vec, new_axes):
        """转换坐标系"""
        A_cur = self.axes.T
        A_new = np.array(new_axes).T
        coords = np.linalg.solve(A_cur, vec)
        return A_new @ coords

    def projection(self, vec):
        """坐标轴投影"""
        coords = self.get_coords(vec)
        projs = []
        for i, c in enumerate(coords):
            proj = abs(c) * np.linalg.norm(self.axes[i])
            projs.append(round(proj, 3))
        return projs

    def angle(self, vec):
        """坐标轴夹角"""
        angles = []
        vec_norm = np.linalg.norm(vec)

        if vec_norm < 1e-10:  # 零向量
            return [0.0] * len(self.axes)

        for axis in self.axes:
            axis_norm = np.linalg.norm(axis)
            if axis_norm < 1e-10:  # 零向量坐标轴
                angles.append(0.0)
                continue

            cos_val = np.dot(vec, axis) / (vec_norm * axis_norm)
            cos_val = max(-1, min(1, cos_val))
            angles.append(round(math.degrees(math.acos(cos_val)), 2))
        return angles

    def area(self):
        """缩放倍数"""
        return round(abs(np.linalg.det(self.axes.T)), 3)


def process_all_groups(filename):
    """处理JSON文件 - 自动检测结构"""
    with open(filename, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        # 列表结构
        print(f"检测到列表结构，共 {len(data)} 个任务组")
        for i, group_data in enumerate(data):
            process_single_group(group_data, f"group_{i + 1}")

    elif isinstance(data, dict) and 'group_name' in data:
        # 单个任务组字典
        process_single_group(data, "single_group")

    elif isinstance(data, dict):
        # 字典包含多个任务组
        for group_key, group_data in data.items():
            process_single_group(group_data, group_key)


def process_single_group(group_data, group_key):
    """处理单个任务组"""
    name = group_data.get('group_name', group_key)
    vectors = group_data.get('vectors', [])
    ori_axis = group_data.get('ori_axis', [])
    tasks = group_data.get('tasks', [])

    if not vectors or not ori_axis or not tasks:
        return

    print(f"处理: {name}")

    for i, vec_data in enumerate(vectors[:3]):
        vec = np.array(vec_data, dtype=float)
        coord = VectorOps(ori_axis)

        print(f"\n向量{i + 1}: {vec_data}")

        # 执行任务序列
        for j, task in enumerate(tasks):
            t = task.get('type')

            if t == 'change_axis':
                new_axes = task.get('obj_axis', [])
                if len(new_axes) > 0:
                    new_vec = coord.change_axis(vec, new_axes)
                    print(f"  [{j + 1}]坐标系转换: {[round(x, 3) for x in new_vec]}")
                    vec = new_vec
                    coord = VectorOps(new_axes)

            elif t == 'axis_projection':
                proj = coord.projection(vec)
                print(f"  [{j + 1}]坐标轴投影: {proj}")

            elif t == 'axis_angle':
                ang = coord.angle(vec)
                print(f"  [{j + 1}]坐标轴夹角: {ang}°")

            elif t == 'area':
                s = coord.area()
                print(f"  [{j + 1}]面积缩放: {s}倍")

    if len(vectors) > 3:
        print(f"\n... 还有 {len(vectors) - 3} 个向量未显示")

process_all_groups("D:\QGdata\data(1).json")