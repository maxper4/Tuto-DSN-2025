class SystemBase:
    required_components_names = set([])
    intrinsic_properties = []

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
        self.properties = self._merge_properties()

    def refresh(self):
        self.properties = self._merge_properties()

    def _merge_properties(self):
        all = list(set([a for _,c in self.components.items() for a in c.properties] + self.intrinsic_properties))
        if "property 1" in all and "property 2" in all:
            all.remove("property 1")
            all.remove("property 2")
            all.append("combination property 1 and 2")
        if "untrusted" in all and self.__class__.__name__ == "FederatedLearning":
            all.append("unscalable")
        if "corrupted" in all and "privacy-preserving" in all:
            all.remove("privacy-preserving")
            all.remove("corrupted")
            all.append("privacy-leaking")
        if "not cool" in all and "cool" in all:
            all.remove("not cool")
        if "untrusted" in all and "trusted" in all:
            all.remove("trusted")
        if "centralized" in all and "decentralized" in all:
            all.remove("decentralized")
        if "data-available" in all and "unavailable" in all:
            all.remove("unavailable")
            all.remove("data-available")
            all.append("available")
        return all
    
    def display(self):
        print(f"{self.name}\nProperties: {', '.join(self.properties)}")
        print("Components:")
        for n, component in self.components.items():
            print(f"{n}: {component.info()}")
        print()

    def info(self):
        return f"{self.name} ({', '.join(self.properties)})"

class Component():
    def __init__(self, name, properties):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        self.name = name
        if not isinstance(properties, list):
            raise TypeError("Properties should be a list")
        if not all(isinstance(attr, str) for attr in properties):
            raise TypeError("All properties should be strings")
        if properties == None:
            raise ValueError("Properties cannot be empty")
        self.properties = properties

    def info(self):
        return f"{self.name} ({', '.join(self.properties)})"

class ExampleSystem(SystemBase):
    required_components_names = set(["Component 1", "Component 2"])
    intrinsic_properties = ["intrinsic property"]

class Blockchain(SystemBase):
    required_components_names = set(["Consensus", "Transactions"]) 
    intrinsic_properties = ["trusted"]

class FederatedLearning(SystemBase):
    required_components_names = set(["Aggregation", "Models Storage"])
    intrinsic_properties = ["privacy-preserving"]

class DistributedStorage(Component):
    def __init__(self):
        super().__init__("Distributed Storage", ["scalable", "unavailable"])

class CentralizedServer(Component):
    def __init__(self):
        super().__init__("Centralized Server", ["untrusted"])
        
    def corrupt(self):
        if "corrupted" not in self.properties:
            self.properties.append("corrupted")
        print("Centralized Server has been corrupted! It will now try to mislead the system.")