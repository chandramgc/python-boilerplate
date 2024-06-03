from faker import Faker
from mongodb_connector import MongoDBConnector

class MongoDBDummyGenerator:
    def __init__(self):
        self.fake = Faker()
        self.db = MongoDBConnector()
        self.customers_collection = self.db['customers']
        self.products_collection = self.db['products']
        self.sales_collection = self.db['sales']

    def generate_customers(self, num_customers):
        customers = []
        for _ in range(num_customers):
            customer = {
                'name': self.fake.name(),
                'email': self.fake.email(),
                'address': self.fake.address(),
                'phone_number': self.fake.phone_number(),
                'job': self.fake.job(),
                'company': self.fake.company()
            }
            customers.append(customer)
        self.customers_collection.insert_many(customers)

    def generate_products(self, num_products):
        products = []
        for _ in range(num_products):
            product = {
                'name': self.fake.word(),
                'price': self.fake.random_int(min=10, max=100),
                'description': self.fake.sentence(),
                'category': self.fake.word(),
                'brand': self.fake.word()
            }
            products.append(product)
        self.products_collection.insert_many(products)

    def generate_sales(self, num_sales):
        sales = []
        for _ in range(num_sales):
            sale = {
                'customer_id': self.fake.random_int(min=1, max=100),
                'product_id': self.fake.random_int(min=1, max=100),
                'quantity': self.fake.random_int(min=1, max=10),
                'date': self.fake.date_time_this_decade(),
                'payment_method': self.fake.random_element(elements=('credit card', 'cash', 'paypal'))
            }
            sales.append(sale)
        self.sales_collection.insert_many(sales)

if __name__ == '__main__':
    generator = MongoDBDummyGenerator()
    generator.generate_customers(10)
    generator.generate_products(20)
    generator.generate_sales(50)
