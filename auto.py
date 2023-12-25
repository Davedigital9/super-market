import pandas as pd

# Load the supermarket_sales dataset
dataset_path = r'C:\Users\HP\Desktop\automation\supermarket_sales.csv'
supermarket_sales = pd.read_csv(dataset_path)

# Display basic information about the dataset
print("First 5 rows of the supermarket_sales dataset:")
print(supermarket_sales.head())

# Display summary statistics
sales_summary = supermarket_sales.describe()
print("\nSummary statistics of the supermarket_sales dataset:")
print(sales_summary)

# Calculate total sales amount
supermarket_sales['Total_Sales'] = supermarket_sales['Total'] - supermarket_sales['Tax 5%']
total_sales_amount = supermarket_sales['Total_Sales'].sum()

# Extract key information: Average rating
average_rating = supermarket_sales['Rating'].mean()

# Calculate total sales for each gender
gender_sales = supermarket_sales.groupby('Gender')['Total'].sum()
print("\nGender-based Sales:")
print(gender_sales)

# Calculate total sales for each product line
product_line_sales = supermarket_sales.groupby('Product line')['Total'].sum()
print("\nProduct Line Sales:")
print(product_line_sales)

# Calculate average rating
average_rating = supermarket_sales['Rating'].mean()
print("\nAverage Rating:", average_rating)

# Calculate total sales for each payment method
payment_method_sales = supermarket_sales.groupby('Payment')['Total'].sum()
print("\nPayment Method Sales:")
print(payment_method_sales)

# Calculate total quantity sold for each product line
quantity_sold = supermarket_sales.groupby('Product line')['Quantity'].sum()
print("\nQuantity Sold:")
print(quantity_sold)

# Calculate total sales for each branch
branch_sales = supermarket_sales.groupby('Branch')['Total'].sum()
print("\nBranch-wise Sales:")
print(branch_sales)

##
# Convert 'Date' column to datetime format
supermarket_sales['Date'] = pd.to_datetime(supermarket_sales['Date'], format='%m/%d/%Y')

# Extract month and year from 'Date' column
supermarket_sales['Month'] = supermarket_sales['Date'].dt.month
supermarket_sales['Year'] = supermarket_sales['Date'].dt.year

# Calculate monthly sales
monthly_sales = supermarket_sales.groupby(['Year', 'Month'])['Total'].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Generate a summary report
summary_report = f"""
Supermarket Sales Dataset Summary:
{sales_summary}

Total Sales Amount: ${total_sales_amount:.2f}

Average Rating: {average_rating:.2f}
"""

# Print the report to the console
print(summary_report)

# Save the report to a text file
with open('supermarket_sales_summary_report.txt', 'w') as file:
    file.write(summary_report)

print("Summary report generated successfully.")
