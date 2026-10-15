def calculate_original_price(purchase_price: float, shipping_fee: float = 0.0, installation_fee: float = 0.0, other_costs: float = 0.0) -> float:
    return float(purchase_price) + float(shipping_fee) + float(installation_fee) + float(other_costs)


def calculate_annual_depreciation(original_price: float, years: int) -> float:
    if years <= 0:
        raise ValueError("Số năm khấu hao phải lớn hơn 0")
    return float(original_price) / int(years)


def calculate_monthly_depreciation(annual_depreciation: float) -> float:
    return float(annual_depreciation) / 12.0


def calculate_yearly_depreciation_details(original_price: float, years: int) -> list:
    if years <= 0:
        raise ValueError("Số năm khấu hao phải lớn hơn 0")

    annual_depreciation = calculate_annual_depreciation(original_price, years)
    accumulated_depreciation = 0.0
    details = []

    for year in range(1, years + 1):
        if year == years:
            current_depreciation = original_price - accumulated_depreciation
            accumulated_depreciation = original_price
            remaining_value = 0.0
        else:
            current_depreciation = annual_depreciation
            accumulated_depreciation += current_depreciation
            remaining_value = original_price - accumulated_depreciation

        details.append({
            "year": year,
            "current_depreciation": current_depreciation,
            "accumulated_depreciation": accumulated_depreciation,
            "remaining_value": remaining_value,
        })

    return details


def get_depreciation_display_lines(original_price: float, years: int) -> list:
    details = calculate_yearly_depreciation_details(original_price, years)
    lines = []
    for item in details:
        rem = item["remaining_value"]
        if abs(rem - round(rem)) < 1e-6:
            rem_str = f"{int(round(rem))}"
        else:
            rem_str = f"{rem:.2f}"
        lines.append(f"Năm {item['year']}, Sau khấu hao còn=>{rem_str}")
    return lines



purchase_price = float(input("Nhập giá mua tài sản: "))
other_costs = float(input("Nhập chi phí vận chuyển, lắp đặt (nhập 0 nếu không có): "))
years = int(input("Nhập số năm khấu hao: "))

original_price = calculate_original_price(purchase_price, other_costs=other_costs)
annual_depreciation = calculate_annual_depreciation(original_price, years)
monthly_depreciation = calculate_monthly_depreciation(annual_depreciation)

print("\n--- THÔNG TIN KHẤU HAO BAN ĐẦU ---")
print(f"Nguyên giá tài sản: {original_price:,.2f}")
print(f"Mức khấu hao hàng năm: {annual_depreciation:,.2f}")
print(f"Mức khấu hao hàng tháng: {monthly_depreciation:,.2f}")

print("\n--- BẢNG KHẤU HAO HÀNG NĂM ---")
print(f"{'Năm':<5} | {'Mức KH năm':<15} | {'KH tích lũy':<15} | {'Giá trị còn lại':<15}")
print("-" * 55)

details = calculate_yearly_depreciation_details(original_price, years)
for row in details:
    print(f"{row['year']:<5} | {row['current_depreciation']:<15,.2f} | {row['accumulated_depreciation']:<15,.2f} | {row['remaining_value']:<15,.2f}")
