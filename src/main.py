from system_base import Component, Blockchain, FederatedLearning

def main():
    tendermint = Component("Tendermint", ["not cool"])
    mempool = Component("Basic Mempool", ["cool"])
    blockchain = Blockchain("Cosmos",{ 
        "Consensus": tendermint, 
        "Mempool": mempool 
    })
    blockchain.display()

    distributed_storage = Component("Distributed Storage", ["redundant", "scalable", "accessible"])

    fl = FederatedLearning("Centralized Federated Learning", {
        "Aggregator": Component("Server", ["secure", "efficient", "not trusted"]),
        "Client": Component("Client", ["privacy-preserving"])
    })
    fl.display()

    dfl = FederatedLearning("Distributed Federated Learning", {
        "Aggregator": blockchain,
        "Client": Component("Client", ["privacy-preserving"])
    })
    dfl.display()

if __name__ == "__main__":
    main()