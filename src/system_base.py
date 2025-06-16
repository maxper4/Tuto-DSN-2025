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

    def _merge_properties(self):
        all = list(set([a for _,c in self.components.items() for a in c.properties] + self.intrinsic_properties))
        if "not cool" in all and "cool" in all:
            all.remove("not cool")
        if "not trusted" in all and "trusted" in all:
            all.remove("trusted")
        if "centralized" in all and "decentralized" in all:
            all.remove("decentralized")
        return all

    def get_properties(self):
        return {
            "name": self.name,
            "properties": self.properties
        }
    
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

class Blockchain(SystemBase):
    required_components_names = set(["Consensus", "Mempool"]) 
    intrinsic_properties = ["decentralized", "trusted"]

class FederatedLearning(SystemBase):
    required_components_names = set(["Aggregation", "Models Storage"])
    intrinsic_properties = ["privacy-preserving"]

class DistributedStorage(SystemBase):
    required_components_names = set(["Proofs"])
    intrinsic_properties = ["scalable", "not-available"]