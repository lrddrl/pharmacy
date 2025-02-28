# 获取药店电话号码（Google Places API）

## 介绍
本项目使用 Google Places API 通过药店名称和地址获取电话号码，并将结果保存到 CSV 文件中。

## 先决条件
在运行本项目之前，请确保你的电脑已安装以下软件：
- **Python**（>= 3.6）
- **pip**（Python 包管理器）

## 安装步骤

### 1. 检查 Python 是否已安装
在电脑的搜索框中，输入 `cmd` 并按回车键（Enter），打开命令提示符（CMD）。

在 CMD 窗口中输入以下命令检查 Python 是否安装：
```sh
python --version
```
如果 Python 已安装，你会看到类似以下的输出：
```
Python 3.x.x
```
如果未安装 Python，请前往 [Python 官网](https://www.python.org/downloads/) 下载并安装。

### 2. 安装依赖包
在 CMD 窗口中，进入本项目所在的文件夹（使用 `cd` 命令，如 `cd C:\Users\你的用户名\Desktop\项目文件夹`）。

然后运行以下命令安装所需的 Python 依赖包：
```sh
pip install -r requirements.txt
```

### 3. 配置 Google API Key

确保 `google_api.txt` 文件和 `fetch_phone_numbers_google.py` 在 **同一个文件夹** 内。

在 `google_api.txt` 文件中粘贴你的 Google Places API Key。

### 4. 准备数据文件
请确保你的数据文件为 `data.csv`，并放置在与脚本相同的文件夹内。

**数据文件格式（示例）**：
```
Pharmacy Name,Address
986 Pharmacy,14501 Magnolia St # 100, Westminster, CA 92683, United States
Providence Infusion,200 W Center Street Promenade Ste 100, Anaheim, CA 92805, United States
```

## 运行脚本

在 CMD 窗口中，进入脚本所在的文件夹，然后运行以下命令执行脚本：
```sh
py fetch_phone_numbers_google.py
```

程序运行后，会自动从 `data.csv` 中读取药店信息，并通过 Google Places API 获取电话号码。获取完成后，结果会保存在 `data_completed.csv` 文件中。

## 运行结果
脚本运行成功后，输出文件 `data_completed.csv` 将包含以下格式的数据：
```
Pharmacy Name,Address,Phone Number
986 Pharmacy,14501 Magnolia St # 100, Westminster, CA 92683, United States,+1 714-123-4567
Providence Infusion,200 W Center Street Promenade Ste 100, Anaheim, CA 92805, United States,+1 714-987-6543
```

## 注意事项
- 确保 `google_api.txt` 文件和 `fetch_phone_numbers_google.py` 在同一文件夹。
- 确保 `data.csv` 文件存在，并且格式正确。
- 每次 API 请求之间有 1 秒延迟，以防止触发 Google API 限制。
- 若 API Key 失效，请在 [Google Cloud 控制台](https://console.cloud.google.com/) 重新申请。

## 贡献
如果你想改进此项目，欢迎提交 Pull Request 或 Issue！🎉

数据表格
![alt text](image-1.png)

完成表格
![alt text](image-2.png)