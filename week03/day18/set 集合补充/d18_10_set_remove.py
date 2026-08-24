# 从 set 删除元素
fault_types = {
    "电池故障",
    "充电故障",
    "通信故障",
    "电机故障"
}
fault_types.remove("通信故障")# 如果你删除一个不存在的元素，会报错。
print(fault_types)
print(len(fault_types))