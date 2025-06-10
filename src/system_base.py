class SystemBase:
    required_components_names = set([])

    def __init__(self, name, components):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        self.name = name
        if not isinstance(components, dict):
            raise TypeError("Components should be a dictionary")
        if self.required_components_names != components.keys():
            raise ValueError(f"Components for {self.name} should be: {self.required_components_names}")
        if not all(isinstance(c, Component) or isinstance(c, SystemBase) for c in components.values()):
            raise TypeError("All components should be instances of Component")
        
        self.components = components
        self.attributes = self._merge_attributes()

    def _merge_attributes(self):
        return list(set([a for _,c in self.components.items() for a in c.attributes]))

    def get_properties(self):
        return {
            "name": self.name,
            "attributes": self.attributes
        }
    
    def display(self):
        print(f"{self.name}\nAttributes: {', '.join(self.attributes)}")
        print("Components:")
        for n, component in self.components.items():
            print(f"{n}: {component.info()}")
        print()

    def info(self):
        return f"{self.name} ({', '.join(self.attributes)})"

class Component():
    def __init__(self, name, attributes):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        self.name = name
        if not isinstance(attributes, list):
            raise TypeError("Attributes should be a list")
        if not all(isinstance(attr, str) for attr in attributes):
            raise TypeError("All attributes should be strings")
        if not attributes:
            raise ValueError("Attributes cannot be empty")
        self.attributes = attributes

    def info(self):
        return f"{self.name} ({', '.join(self.attributes)})"

class Blockchain(SystemBase):
    required_components_names = set(["Consensus", "Mempool"])

class FederatedLearning(SystemBase):
    required_components_names = set(["Aggregator", "Client"])