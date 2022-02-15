def bouquets(narcissus_price, tulip_price, rose_price, summ):
    price_list = sorted([narcissus_price, tulip_price, rose_price], reverse = True)
    counter = 0
    for a in range(int(summ//price_list[0]) + 1):
        for b in range(int((summ - a * price_list[0])//price_list[1]) + 1):
            for c in range(int((summ - a * price_list[0] - b * price_list[1])//price_list[2]) + 1):
                if (a + b + c) % 2:
                    if a * price_list[0] + b * price_list[1] + c * price_list[2] <= summ:
                        counter += 1
    return counter
print(bouquets(21.25,13.6,10.5,100))
