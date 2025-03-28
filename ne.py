class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity):

        return self.stock >= quantity

    def reduce_stock(self, quantity):

        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):

        if product.is_available(quantity):
            if product.name in self.items:
                self.items[product.name]["quantity"] += quantity
            else:
                self.items[product.name] = {"product": product, "quantity": quantity}
            product.reduce_stock(quantity)
            print(f"{quantity} шт. {product.name} добавлено в корзину")
        else:
            print(f"нехватает товара {product.name} товар еще есть")

    def remove_product(self, product_name):

        if product_name in self.items:
            product = self.items[product_name]["product"]
            quantity = self.items[product_name]["quantity"]
            product.stock += quantity
            del self.items[product_name]
            print(f"{product_name} удалено из корзины")
        else:
            print("этого товара нет в корзине")

    def get_total_price(self):

        total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return total

    def show_cart(self):

        if not self.items:
            print("корзина пустая")
        else:
            print("Ваша корзина:")
            for name, item in self.items.items():
                print(f"{name}: {item['quantity']} шт. - {item['product'].price} грн за шт.")
            print(f"полная цена: {self.get_total_price()} грн")

# Приклад використання
p1 = Product("Ноутбук", 30000, 5)
p2 = Product("Смартфон", 15000, 10)

cart = Cart()
cart.add_product(p1, 2)
cart.add_product(p2, 1)
cart.show_cart()
cart.remove_product("Ноутбук")
cart.show_cart()
