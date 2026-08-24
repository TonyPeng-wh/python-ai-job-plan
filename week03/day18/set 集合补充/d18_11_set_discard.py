# discard()
fault_types = {
    "电池故障",
    "充电故障",
    "通信故障"
}
fault_types.discard("充电故障")
fault_types.discard("传感器故障")
print(fault_types)
print(len(fault_types))

# remove → 不存在会报错
# discard → 不存在也没事