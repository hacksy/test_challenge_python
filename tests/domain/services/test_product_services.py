from unittest import TestCase
from unittest.mock import create_autospec, patch

from data.repository.discount_repository import DiscountRepository
from data.repository.product_repository import ProductRepository
from domain.services.products_services import ProductsService


class TestProductService(TestCase):
    productRepository: ProductRepository
    productService: ProductsService
    discountRepository: DiscountRepository

    def setUp(self):
        super().setUp()
        self.productRepository = create_autospec(
            ProductRepository
        )
        self.discountRepository = create_autospec(
            DiscountRepository
        )

        self.productService = ProductsService(
            product_repository=self.productRepository,
            discount_repository=self.discountRepository,
        )

    @patch(
        "presentation.schema.request.create_product_schema.CreateProductSchema",
        autospec=True,
    )
    def test_create_product(self, CreateProductSchema):
        product = CreateProductSchema()
        product.name = "TestProduct"
        product.status = 1
        product.stock = 1
        product.description = "TestProduct"
        product.price = 10
        self.productService.create_product(product)
        self.productRepository.add.assert_called_once()
        self.discountRepository.get_discount.assert_called_once()

    def test_get_product(self):
        self.productService.get_product_by_id(product_id='uuid')
        self.productRepository.get_by_id.assert_called_once()

    @patch(
        "presentation.schema.request.create_product_schema.CreateProductSchema",
        autospec=True,
    )
    def test_update_product(self, CreateProductSchema):
        product = CreateProductSchema()
        product.name = "SecondTestProduct"

        self.productService.update_product(
            product_id='uuid', product=product
        )

        self.productRepository.update_by_id.assert_called_once()

    def test_delete_product(self):
        self.productService.delete_product_by_id(product_id='uuid')
        self.productRepository.delete_by_id.assert_called_once()

    def test_list_all_products(self):
        self.productService.get_products()

        # Should call list method on Product Repository
        self.productRepository.get_all.assert_called_once()
