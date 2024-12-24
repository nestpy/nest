import pytest
from src.nest.core.container import Container
from src.nest.common.decorators.core.injectable import Injectable

# Clases de prueba
@Injectable()
class ServiceA:
    def get_name(self):
        return "ServiceA"

@Injectable()
class ServiceB:
    def __init__(self, service_a: ServiceA):
        self.service_a = service_a

    def get_name(self):
        return f"ServiceB with {self.service_a.get_name()}"

class NonInjectableService:
    pass

@pytest.fixture
def container():
    return Container()

class TestContainer:
    def test_container_initialization(self, container):
        """Test que el contenedor se inicializa correctamente"""
        assert container._services == {}

    def test_register_injectable_service(self, container):
        """Test que registra correctamente un servicio inyectable"""
        service = container.register(ServiceA)
        assert isinstance(service, ServiceA)
        assert service.get_name() == "ServiceA"
        assert ServiceA in container._services

    def test_register_non_injectable_service(self, container):
        """Test que falla al registrar un servicio no inyectable"""
        with pytest.raises(ValueError) as exc:
            container.register(NonInjectableService)
        assert "must be decorated with @Injectable()" in str(exc.value)

    def test_get_existing_service(self, container):
        """Test que obtiene un servicio existente"""
        service1 = container.register(ServiceA)
        service2 = container.get(ServiceA)
        assert service1 is service2  # Verifica que es la misma instancia

    def test_get_non_existing_service(self, container):
        """Test que registra y obtiene un servicio no existente"""
        service = container.get(ServiceA)
        assert isinstance(service, ServiceA)
        assert ServiceA in container._services

    def test_dependency_injection(self, container):
        """Test que maneja correctamente la inyección de dependencias"""
        service_b = container.get(ServiceB)
        assert isinstance(service_b, ServiceB)
        assert isinstance(service_b.service_a, ServiceA)
        assert service_b.get_name() == "ServiceB with ServiceA"

    def test_singleton_behavior(self, container):
        """Test que verifica el comportamiento singleton de los servicios"""
        service1 = container.get(ServiceA)
        service2 = container.get(ServiceA)
        assert service1 is service2

    def test_circular_dependency(self, container):
        """Test que maneja correctamente las dependencias circulares"""
        @Injectable()
        class ServiceC:
            def __init__(self, service_d: 'ServiceD'):
                self.service_d = service_d

        @Injectable()
        class ServiceD:
            def __init__(self, service_c: ServiceC):
                self.service_c = service_c

        # Debería lanzar una excepción o manejar la dependencia circular
        with pytest.raises(Exception):
            container.get(ServiceC)

    def test_empty_constructor(self, container):
        """Test que maneja correctamente servicios sin constructor"""
        @Injectable()
        class EmptyService:
            pass

        service = container.get(EmptyService)
        assert isinstance(service, EmptyService)

    def test_constructor_without_annotations(self, container):
        """Test que falla cuando un servicio no tiene anotaciones de tipo en sus parámetros"""
        @Injectable()
        class NoAnnotationService:
            def __init__(self, service):  # Sin anotación de tipo
                self.service = service

        with pytest.raises(ValueError) as exc:
            container.get(NoAnnotationService)
        assert "All constructor parameters must have type annotations" in str(exc.value)
  