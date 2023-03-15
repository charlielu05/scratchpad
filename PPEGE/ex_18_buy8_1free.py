# 9th item is free

def get_cost_of_cofee(number_of_items:int, price_of_item: float)->float:
    if number_of_items <= 8:
        return number_of_items * price_of_item
    else:
        return (number_of_items * price_of_item) - ((number_of_items // 9) * price_of_item)

if __name__ == "__main__":
    assert get_cost_of_cofee(7, 2.50) == 17.50
    assert get_cost_of_cofee(10, 2.50) == 22.50
    assert get_cost_of_cofee(9, 2.50) == 20