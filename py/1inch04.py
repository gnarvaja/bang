import requests
import matplotlib.pyplot as plt

def get_slippage(api_url, headers, params, actual_dst_amount):
    # 发起请求
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()

    # 获取目标代币数量
    dst_amount = int(data['dstAmount'])
    src_amount = int(params['amount'])

    # 计算预期汇率
    expected_rate = dst_amount / src_amount

    # 计算实际汇率
    actual_rate = actual_dst_amount / src_amount

    # 计算滑点
    slippage_percentage = abs(expected_rate - actual_rate) / expected_rate * 100

    return expected_rate, actual_rate, slippage_percentage

def plot_slippage(chain_ids, slippages):
    plt.figure(figsize=(10, 6))
    plt.bar(chain_ids, slippages, color='skyblue')
    plt.xlabel("Chain ID")
    plt.ylabel("Slippage (%)")
    plt.title("Slippage Comparison Across Chains")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for i, v in enumerate(slippages):
        plt.text(i, v + 0.2, f"{v:.2f}%", ha='center', fontsize=10)
    plt.show()

def main():
    # 定义多个链的地址信息
    chains = [
        {
            "chain_id": 1,
            "api_url": "https://api.1inch.dev/swap/v6.0/1/quote",
            "src_token": "0x514910771af9ca656af840dff83e8264ecf986ca",
            "dst_token": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "amount": "100000000000000000000000000",
            "actual_dst_amount": 2000000000000000000000000
        },
        {
            "chain_id": 56,
            "api_url": "https://api.1inch.dev/swap/v6.0/56/quote",
            "src_token": "0xf8a0bf9cf54bb92f17374d9e9a321e6a111a51bd",
            "dst_token": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
            "amount": "100000000000000000000000000",
            "actual_dst_amount": 2000000000000000000000000
        },
        {
            "chain_id": 137,
            "api_url": "https://api.1inch.dev/swap/v6.0/137/quote",
            "src_token": "0x53e0bca35ec356bd5dddfebbd1fc0fd03fabad39",
            "dst_token": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            "amount": "100000000000000000000000000",
            "actual_dst_amount": 2000000000000000000000000

        }
    ]

    # 设置请求头
    headers = {
        "Authorization": "BiKttlYm0UXzkJMTAlgeh6ucvRXsih7K"
    }

    chain_ids = []
    slippages = []

    # 遍历每个链计算滑点
    for chain in chains:
        params = {
            "src": chain["src_token"],
            "dst": chain["dst_token"],
            "amount": chain["amount"]
        }

        try:
            expected_rate, actual_rate, slippage = get_slippage(
                api_url=chain["api_url"],
                headers=headers,
                params=params,
                actual_dst_amount=chain["actual_dst_amount"]
            )

            chain_ids.append(chain["chain_id"])
            slippages.append(slippage)

            print(f"Chain ID: {chain['chain_id']}")
            print(f"Expected Rate: {expected_rate}")
            print(f"Actual Rate: {actual_rate}")
            print(f"Slippage: {slippage}%\n")

        except Exception as e:
            print(f"Error processing chain {chain['chain_id']}: {e}\n")
    
    # 绘制滑点柱状图
    plot_slippage(chain_ids, slippages)

if __name__ == "__main__":
    main()
