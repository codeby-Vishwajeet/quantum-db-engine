import unittest
from cluster.node_manager import ClusterTopologyCoordinator

class TestClusterTopology(unittest.TestCase):
    def test_raft_consensus_state(self):
        coordinator = ClusterTopologyCoordinator()
        sync = coordinator.perform_heartbeat_sync()
        self.assertEqual(sync["cluster_consensus"], "RAFT-VALIDATED")
