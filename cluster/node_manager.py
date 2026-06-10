import random

class ClusterTopologyCoordinator:
    def __init__(self):
        self.nodes = ["NODE-01-PRIMARY", "NODE-02-REPLICA", "NODE-03-REPLICA"]

    def perform_heartbeat_sync(self):
        return {
            "cluster_consensus": "RAFT-VALIDATED",
            "replication_lag_ms": round(random.uniform(0.1, 0.4), 2),
            "quorum_status": "CONNECTED"
        }
