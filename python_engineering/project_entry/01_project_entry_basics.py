import os
import json


def load_fault_data(data_file_path):
    try:
        # 根据文件路径打开 JSON 文件
        with open(
            data_file_path,
            "r",
            encoding="utf-8"
        ) as file:
            # 把 JSON 文件中的数据解析成 Python 数据
            fault_data = json.load(file)
        
    except FileNotFoundError as error:
        print(f"数据文件不存在：{error}")
        return []
    
    except json.JSONDecodeError as error:
        # 文件存在，但是 JSON 格式不正确
        print(f"JSON 数据格式错误：{error}")
        return []

    
     # 读取成功后返回故障数据
    return fault_data

def analyze_fault_data(fault_data):
    # 统计故障数据数量
    fault_count = len(fault_data)

    # 返回故障数量
    return fault_count


def main():
    # 获取当前 Python 文件的绝对路径
    script_file_path = os.path.abspath(__file__)

    # 获取当前 Python 文件所在的目录
    script_directory = os.path.dirname(script_file_path)

    # 从当前脚本目录向上两层，得到项目根目录
    project_root = os.path.abspath(
        os.path.join(script_directory, "..", "..")
    )

    # 拼接出 fault_data.json 的完整路径
    data_file_path = os.path.join(
        project_root,
        "data",
        "fault_data.json"
    )

    # 把文件路径传给读取函数，并接住返回的故障数据
    fault_data = load_fault_data(data_file_path)

    # 把故障数据传给分析函数，并接住返回的故障数量
    fault_count = analyze_fault_data(fault_data)

    # 输出统计结果
    print(f"故障数量：{fault_count}")


if __name__ == "__main__":
    # 程序入口
    main()