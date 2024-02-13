import pandas as pd

dictionary = {
    "Category": [
        "Clothing",
        "Clothing",
        "Shoes",
        "Accessories",
        "Shoes",
        "Clothing",
        "Accessories",
        "Accessories",
        "Shoes",
        "Clothing",
    ],
    "Product": [
        "Sweater",
        "T-shirt",
        "Sandals",
        "Earrings",
        "Sneakers",
        "Pants",
        "Necklace",
        "Ring",
        "Boots",
        "Jacket",
    ],
    "Price": [300, 180, 450, 50, 700, 400, 150, 80, 850, 900],
}

df = pd.DataFrame(dictionary)

print(f"\nCategory at the 2nd index is: {df.iloc[2]['Category']}")
print(f"Product at the 2nd index is : {df.iloc[2]['Product']}")
print(f"\nAll elements from index 4-9 is :\n{df[2:10]}")
print(f"\nAll products from index 1-6 is :\n{df.iloc[1:7]['Product']}")

print(
    f"""\nAll products at the clothing category is:
{df[df['Category'] == 'Clothing']['Product']}"""
)
print(
    f"""\nAll products at the shoes category is:
{df[df['Category'] == 'Shoes']['Product']}"""
)
print(
    f"""\nAll products at the accessories category is:
{df[df['Category'] == 'Accessories']['Product']}"""
)

print(df)
print(
    f"""All products in the clothing category with the price greater than 300 is:
{df[(df['Category'] == 'Clothing') & (df['Price'] > 300)]['Product']}"""
)
print(
    f"""\nAll products in the shoes category with the price less than 600 is:
{df[(df['Category'] == 'Shoes') & (df['Price'] < 600)]['Product']}"""
)
print(
    f"""\nAll products in the accessories category with the price greater than 100 is:
{df[(df['Category'] == 'Accessories') & (df['Price'] > 100)]['Product']}"""
)
