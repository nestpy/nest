import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.nest.core.application import Application
from src.nest.common.decorators.core.module import Module
from src.nest.common.decorators.core.controller import Controller
from src.nest.common.decorators.core.injectable import Injectable
from src.nest.common.decorators.http.request_mapping import Get

# Fixtures y clases de prueba
@Controller("/test")
class TestController:
    @Get()
    async def get_test(self): #TODO: Create method not async
        return {"message": "test"}

@Module(
    controllers=[TestController],
)
class TestModule:
    pass

@pytest.fixture
def app():
    return Application(FastAPI())

class TestApplication:
    def test_init(self, app):
        """Test de inicialización básica"""
        assert isinstance(app.app, FastAPI)
        assert len(app.modules) == 0
        assert len(app.controllers) == 0
        assert app.global_prefix == ""
        assert app.versioning_options is None

    def test_create_module(self, app):
        """Test de creación de módulo"""
        app.create_module(TestModule)
        
        assert TestModule in app.modules
        assert len(app.controllers) == 1
        assert TestController in app.controllers

    def test_create_module_without_decorator(self, app):
        """Test que verifica que falla al crear un módulo sin decorador"""
        class InvalidModule:
            pass

        with pytest.raises(ValueError) as exc:
            app.create_module(InvalidModule)
        assert "must be decorated with @Module()" in str(exc.value)

    def test_set_global_prefix(self, app):
        """Test de configuración del prefijo global"""
        app.set_global_prefix("/api")
        assert app.global_prefix == "/api"

        # Prueba normalización de prefijos
        app.set_global_prefix("api/")
        assert app.global_prefix == "/api"

    def test_normalize_path(self, app):
        """Test de normalización de rutas"""
        assert app._normalize_path("api", "users") == "/api/users"
        assert app._normalize_path("/api/", "/users/") == "/api/users"
        assert app._normalize_path("", "users") == "/users"
        assert app._normalize_path() == ""

    def test_register_routes(self, app):
        """Test de registro de rutas"""
        app.create_module(TestModule)
        app._register_routes()
        
        client = TestClient(app.app)
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"message": "test"}

    def test_versioning(self, app):
        """Test de versionado de rutas"""
        app.enable_versioning(
            prefix="v",
            default_version="1"
        )
        app.create_module(TestModule)
        app._register_routes()

        client = TestClient(app.app)
        response = client.get("/v1/test")
        assert response.status_code == 200
        assert response.json() == {"message": "test"}

    def test_global_prefix_with_versioning(self, app):
        """Test de prefijo global con versionado"""
        app.set_global_prefix("/api")
        app.enable_versioning(
            prefix="v",
            default_version="1"
        )
        app.create_module(TestModule)
        app._register_routes()

        client = TestClient(app.app)
        response = client.get("/api/v1/test")
        assert response.status_code == 200
        assert response.json() == {"message": "test"}

    @pytest.mark.asyncio
    async def test_init_and_close(self, app):
        """Test de inicialización y cierre de la aplicación"""
        await app.init()  # No debería lanzar errores
        await app.close()  # No debería lanzar errores

    def test_get_http_adapter(self, app):
        """Test para obtener el adaptador HTTP"""
        adapter = app.get_http_adapter()
        assert isinstance(adapter, FastAPI) 

    def test_create_module_with_imports(self, app):
        """Test de creación de módulo con importaciones"""
        @Module(imports=[TestModule])
        class ImportingModule:
            pass

        app.create_module(ImportingModule)
        assert ImportingModule in app.modules
        assert TestModule in app.modules

    def test_set_global_prefix(self, app):
        """Test de configuración del prefijo global"""
        app.set_global_prefix("/api")
        assert app.global_prefix == "/api"

    def test_enable_versioning(self, app):
        """Test de habilitación de versionado"""
        app.enable_versioning(prefix="v", default_version="1")
        assert app.versioning_options["prefix"] == "v"
        assert app.versioning_options["default_version"] == "1"

    def test_instantiate_controller(self, app):
        """Test de instanciación de controlador"""
        controller = app._instantiate_controller(TestController)
        assert isinstance(controller, TestController)

    def test_register_routes(self, app):
        """Test de registro de rutas"""
        app.create_module(TestModule)
        app._register_routes()
        
        client = TestClient(app.app)
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"message": "test"}

    @pytest.mark.asyncio
    async def test_create_route_handler(self, app):
        """Test de creación de manejador de ruta"""
        async def dummy_handler():
            return {"message": "dummy"}
    
        handler = app._create_route_handler(dummy_handler)
        response = await handler()
        assert response.body == b'{"message":"dummy"}'
        assert response.status_code == 200

    def test_get_http_adapter(self, app):
        """Test para obtener el adaptador HTTP"""
        adapter = app.get_http_adapter()
        assert isinstance(adapter, FastAPI)

    def test_register_routes_with_versioning(self, app):
        """Test de registro de rutas con versionado"""
        app.enable_versioning(prefix="v", default_version="1")
        app.create_module(TestModule)
        app._register_routes()

        client = TestClient(app.app)
        response = client.get("/v1/test")
        assert response.status_code == 200
        assert response.json() == {"message": "test"}

    def test_create_module_with_metadata_imports(self, app):
        """Test de creación de módulo con importaciones"""
        @Module(imports=[TestModule])
        class ImportingModule:
            pass

        app.create_module(ImportingModule)
        assert ImportingModule in app.modules
        assert TestModule in app.modules

    def test_instantiate_controller_with_dependencies(self, app):
        """Test de instanciación de controlador con dependencias"""

        @Injectable()
        class DependencyService:
            def get_dependency(self):
                return "dependency"

        @Controller("/dependency")
        class DependencyController:
            def __init__(self, service: DependencyService):
                self.service = service

            @Get()
            async def get_service(self):
                return {"service": self.service.get_dependency()}

        @Module(controllers=[DependencyController], providers=[DependencyService])
        class DependencyModule:
            pass

        app.create_module(DependencyModule)
        app._register_routes()

        client = TestClient(app.app)
        response = client.get("/dependency")
        assert response.status_code == 200
        assert response.json() == {"service": "dependency"}

    @pytest.mark.asyncio
    async def test_init(self, app):
        """Test de inicialización de la aplicación"""
        await app.init()  # No debería lanzar errores

    @pytest.mark.asyncio
    async def test_close(self, app):
        """Test de cierre de la aplicación"""
        await app.close()  # No debería lanzar errores

    def test_get_http_adapter(self, app):
        """Test para obtener el adaptador HTTP"""
        adapter = app.get_http_adapter()
        assert isinstance(adapter, FastAPI)

    def test_register_routes(self, app):
        """Test de registro de rutas"""
        app.create_module(TestModule)
        app._register_routes()
        
        client = TestClient(app.app)
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"message": "test"}