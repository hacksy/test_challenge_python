"""Containers module."""
from dependency_injector import containers, providers
import logging.config

from config.database import Database
from data.repository.cache_repository import CacheRepository
from data.repository.product_repository import ProductRepository
from data.repository.discount_repository import DiscountRepository
from data.repository.time_logger_repository import TimeLoggerRepository
from domain.services.products_services import ProductsService


class Container(containers.DeclarativeContainer):
    """ Configuration and DI """
    wiring_config = containers.WiringConfiguration(modules=["presentation.endpoints.product_endpoints"])

    config = providers.Configuration(yaml_files=["config.yml"])
    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )
    db = providers.Singleton(Database, db_url=config.db.url)

    product_repository = providers.Factory(
        ProductRepository,
        session_factory=db.provided.session,
    )

    discount_repository = providers.Factory(
        DiscountRepository,
    )

    products_service = providers.Factory(
        ProductsService,
        product_repository=product_repository,
        discount_repository=discount_repository,
    )

    cache_repository = providers.Factory(
        CacheRepository
    )
    timer = providers.Factory(
        TimeLoggerRepository
    )
