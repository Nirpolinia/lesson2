def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
    except (ValueError,TypeError):
        return ("Ожидается ввод числа")
    try:
        max_discount = abs(int(max_discount))
    except (ValueError,TypeError):
        return ("Ожидается ввод числа_")
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
print (discounted (11,12))
        

