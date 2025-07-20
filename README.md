# optimal-basket-split


This project provides an algorithm and Python implementation for maximizing discounts when purchasing products under a discount system commonly used in consumer electronics stores in Poland.
It finds the best way to split a list of product prices into baskets, so that the total discount is as large as possible.

## Features

- Reads product prices from a text file (one price per line, supports decimals).
- Applies basket-based discount rules:
  - 2 products: 30% off the cheapest
  - 3 products: 55% off the cheapest
  - 4 products: 80% off the cheapest
  - 5 products: cheapest for 1 PLN
- Finds the optimal split of products into baskets to maximize total discount.
- Prints detailed basket summaries and overall totals.

## Usage

1. **Prepare your input file**  
   Create a file named `list_of_products.txt` in the project directory, with each product price on a separate line, e.g.:
   ```
   100.00
   200.50
   300.99
   400.00
   ```

2. **Run the program**
   ```bash
   python3 optimal_basket_split.py
   ```

3. **View the output**
   The program will print basket breakdowns and a summary of total prices and discounts.

## Example Output

```
Basket 1: ['100.00', '200.50']
  Total before discount: 300.50 PLN
  Total after discount:  270.50 PLN
  Discount:              30.00 PLN

Basket 2: ['300.99', '400.00']
  Total before discount: 700.99 PLN
  Total after discount:  610.69 PLN
  Discount:              90.30 PLN

Summary:
  Total before discount: 1001.49 PLN
  Total after discount:  881.19 PLN
  Total discount:        120.30 PLN
```

## How it works

The algorithm uses recursion and memoization to efficiently explore all possible ways to split the products into baskets of 2–5 items, applying the discount rules to each basket.  
It selects the split that yields the highest total discount.

## Requirements

- Python 3.7+
- No external dependencies

## License

MIT License

## Contributing

Pull requests and suggestions