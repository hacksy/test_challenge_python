import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models.product_model import Product

from config.database import Base


class ProductTestQuery(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)
        self.panel = Product(product_id='uuid', name='Test Product', discount=10, description='None', price=999,
                             status=0,
                             stock=30)
        self.session.add(self.panel)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_product_is_retrieved(self):
        product = self.session.query(Product).first()
        self.assertEqual(product.product_id, 'uuid')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.discount, 10)
        self.assertEqual(product.description, 'None')
        self.assertEqual(product.price, 999)
        self.assertEqual(product.status, 0)
        self.assertEqual(product.stock, 30)
        self.assertEqual(product.final_price, 899.1)

    def test_product_repr_is_correct(self):
        product = self.session.query(Product).first()
        repr = product.__repr__()
        self.assertEqual(repr,
                         '<ProductModel(productId=uuid, name="Test Product", status="False", final_price="899.1", description=None)>')
