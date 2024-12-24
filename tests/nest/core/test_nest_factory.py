import pytest
from fastapi import FastAPI
from src.nest.core.nest_factory import NestFactory
from src.nest.core.application import Application
from src.nest.common.decorators.core.module import Module

@Module()
class TestModule:
    """Módulo de prueba para los tests"""
    pass

class TestNestFactory:
    def test_create_returns_application(self):
        """
        Test que verifica que create() devuelve una instancia de Application
        """
        app = NestFactory.create(TestModule)

        assert isinstance(app, Application)
        assert isinstance(app.app, FastAPI)

    def test_create_configures_module(self):
        """
        Test que verifica que create() configura el módulo correctamente
        """
        app = NestFactory.create(TestModule)
        
        assert app.modules == { TestModule }

    @pytest.mark.asyncio
    async def test_create_microservice_not_implemented(self ):
        """
        Test que verifica que create_microservice() está pendiente de implementar
        """
        result = await NestFactory.create_microservice(TestModule)
        assert result is None

    @pytest.mark.asyncio
    async def test_create_application_context_not_implemented(self):
        """
        Test que verifica que create_application_context() está pendiente de implementar
        """
        result = await NestFactory.create_application_context(TestModule)
        assert result is None 