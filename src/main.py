from system_base import Component, Blockchain, FederatedLearning, DistributedStorage

def main():
    tendermint = Component("Tendermint", ["not cool"])
    mempool = Component("Basic Mempool", ["cool"])
    blockchain = Blockchain("Cosmos", { 
        "Consensus": tendermint, 
        "Mempool": mempool 
    })
    blockchain.display()

    centralized_server = Component("Centralized Server", ["centralized", "not trusted"])
    fl = FederatedLearning("Centralized Federated Learning", {
        "Aggregation": centralized_server,
        "Models Storage": blockchain
    })
    fl.display()

    dfl = FederatedLearning("Distributed Federated Learning", {
        "Aggregation": blockchain,
        "Models Storage": blockchain
    })
    dfl.display()

    empty = Component("Empty", [])

    ds = DistributedStorage("Zenoh", {
        "Proofs": empty,
    })
    ds.display()

if __name__ == "__main__":
    main()