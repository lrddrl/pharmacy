import requests
import pandas as pd
import time
from tqdm import tqdm

# 从 google api.txt 读取 API Key
with open("google api.txt", "r") as f:
    GOOGLE_PLACES_API_KEY = f.read().strip()

# 读取 CSV 文件
file_path = "data.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# 通过 Google Places API 获取电话号码
def get_phone_number(pharmacy_name, address):
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"

    # 查询药店
    search_params = {
        "query": f"{pharmacy_name}, {address}",
        "key": GOOGLE_PLACES_API_KEY
    }

    search_response = requests.get(search_url, params=search_params).json()
    time.sleep(1)  # 防止 API 速率限制

    if "results" in search_response and len(search_response["results"]) > 0:
        place = search_response["results"][0]  # 获取第一个搜索结果
        place_id = place["place_id"]

        # 处理永久关闭的情况
        if place.get("business_status") == "CLOSED_PERMANENTLY":
            return "已永久关闭"

        # 通过 Place ID 获取详细信息
        details_params = {
            "place_id": place_id,
            "fields": "formatted_phone_number",
            "key": GOOGLE_PLACES_API_KEY
        }

        details_response = requests.get(details_url, params=details_params).json()
        time.sleep(1)  # 防止 API 速率限制

        if "result" in details_response and "formatted_phone_number" in details_response["result"]:
            return details_response["result"]["formatted_phone_number"]

    return "N/A"  # 没找到返回 "N/A"

# 遍历所有药店，获取电话号码，并添加进度条
tqdm.pandas(desc="Fetching phone numbers")
df["Phone Number"] = df.progress_apply(lambda row: get_phone_number(row["Pharmacy Name"], row["Address"]), axis=1)

# 保存新 CSV 文件
output_path = "data_completed.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ 已生成新的 CSV 文件: {output_path}")
