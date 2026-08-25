# 给 set 添加元素。
fault_types = {
    "电池故障",
    "充电故障"
}
fault_types.add("通信故障")
fault_types.add("电池故障")
print(fault_types)
print(len(fault_types))