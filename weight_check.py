# Validate pool weight distribution allocations for an index token
def validate_allocations(pools):
    total_weight = sum(pools.values())
    return total_weight == 100, total_weight

asset_distribution = {"ETH": 50, "WBTC": 30, "USDC": 20}
is_valid, current_sum = validate_allocations(asset_distribution)

print(f"Total Allocation Sum: {current_sum}%")
print(f"Is Portfolio Configuration Valid? {is_valid}")
