from itertools import combinations
from functools import lru_cache
from typing import List, Tuple

def calculate_discount(basket: List[float]) -> float:
    """
    Calculate the discount for a basket based on its size.
    Only the cheapest item receives the discount.
    """
    if not basket:
        return 0.0
    cheapest = min(basket)
    n = len(basket)
    if n == 2:
        return cheapest * 0.3
    elif n == 3:
        return cheapest * 0.55
    elif n == 4:
        return cheapest * 0.8
    elif n == 5:
        return cheapest - 1.0
    return 0.0

def read_prices(filename: str) -> List[float]:
    """
    Read product prices from a file, one price per line.
    Returns a list of floats.
    """
    prices = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().replace(',', '.')
            if line:
                try:
                    prices.append(float(line))
                except ValueError:
                    raise ValueError(f"Invalid price value: {line}")
    return prices

def tupled(items: List[float]) -> Tuple[float, ...]:
    """
    Convert a list of floats to a sorted tuple for memoization.
    """
    return tuple(sorted(items))

@lru_cache(maxsize=None)
def max_discount(prices_tuple: Tuple[float, ...]) -> Tuple[float, List[List[float]]]:
    """
    Recursively find the split of baskets that maximizes total discount.
    Returns the maximum discount and the corresponding basket split.
    """
    prices = list(prices_tuple)
    n = len(prices)
    if n < 2:
        return 0.0, []
    best_discount = 0.0
    best_split: List[List[float]] = []
    for k in range(2, min(6, n + 1)):
        for basket_idx in combinations(range(n), k):
            basket = [prices[i] for i in basket_idx]
            remaining = [prices[i] for i in range(n) if i not in basket_idx]
            basket_discount = calculate_discount(basket)
            remaining_discount, remaining_split = max_discount(tupled(remaining))
            total_discount = basket_discount + remaining_discount
            if total_discount > best_discount:
                best_discount = total_discount
                best_split = [basket] + remaining_split
    return best_discount, best_split

def print_basket_summary(basket: List[float], index: int) -> Tuple[float, float, float]:
    """
    Print summary for a single basket and return its totals.
    """
    basket_sum = sum(basket)
    basket_discount = calculate_discount(basket)
    basket_after_discount = basket_sum - basket_discount
    print(f"Basket {index}: {[f'{c:.2f}' for c in basket]}")
    print(f"  Total before discount: {basket_sum:.2f} PLN")
    print(f"  Total after discount:  {basket_after_discount:.2f} PLN")
    print(f"  Discount:              {basket_discount:.2f} PLN\n")
    return basket_sum, basket_after_discount, basket_discount

def main():
    prices = read_prices('list_of_products.txt')
    best_discount, best_split = max_discount(tupled(prices))

    total_before_discount = 0.0
    total_after_discount = 0.0
    total_discounts = 0.0

    for i, basket in enumerate(best_split, 1):
        before, after, discount = print_basket_summary(basket, i)
        total_before_discount += before
        total_after_discount += after
        total_discounts += discount

    print("Summary:")
    print(f"  Total before discount: {total_before_discount:.2f} PLN")
    print(f"  Total after discount:  {total_after_discount:.2f} PLN")
    print(f"  Total discount:        {total_discounts:.2f} PLN")

if __name__ == "__main__":
    main()