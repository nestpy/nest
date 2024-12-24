from src.nest.common.decorators.core.module import Module
from src.nest.common.decorators.core.module import ModuleMetadata

def test_module_decorator():
    """
    Test that verifies the Module decorator properly configures a module with all options.
    
    It checks:
    - The __module__ attribute is set to True
    - The metadata contains correct controllers
    - The metadata contains correct providers
    - The metadata contains correct imports
    - The metadata contains correct exports
    """
    class Service1: pass
    class Service2: pass
    class Controller1: pass
    class SubModule: pass

    @Module(
        controllers=[Controller1],
        providers=[Service1, Service2],
        imports=[SubModule],
        exports=[Service1]
    )
    class TestModule:
        pass

    assert hasattr(TestModule, "__module__")
    assert TestModule.__module__ is True
    
    metadata: ModuleMetadata = TestModule.__metadata__
    assert metadata.controllers == [Controller1]
    assert metadata.providers == [Service1, Service2]
    assert metadata.imports == [SubModule]
    assert metadata.exports == [Service1]

def test_module_decorator_empty():
    """
    Test that verifies the Module decorator works with no arguments.
    
    It checks:
    - The __module__ attribute is set to True
    - All metadata lists are initialized as empty lists
    """
    @Module()
    class TestModule:
        pass

    assert hasattr(TestModule, "__module__")
    metadata: ModuleMetadata = TestModule.__metadata__
    assert metadata.controllers == []
    assert metadata.providers == []
    assert metadata.imports == []
    assert metadata.exports == []
