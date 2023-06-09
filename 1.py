def count_purchases():
    n = int(input("Введите количество записей о покупке: "))
    purchases = {}

    for _ in range(n):
        record = input("Введите запись о покупке (format: 'Покупатель Товар Количество'): ")
        customer, item, quantity = record.split()
        if customer in purchases:
            purchases[customer].append((item, int(quantity)))
        else:
            purchases[customer] = [(item, int(quantity))]

    for customer, items in purchases.items():
        print(customer + ":")
        for item, quantity in items:
            print(item, quantity)


count_purchases()

