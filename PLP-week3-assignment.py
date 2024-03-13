def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
    else:
        final_price = price
    return final_price

def main():
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    print(f"The final price after applying the discount is: {final_price}")

if __name__ == "__main__":
    main()
