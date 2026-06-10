import unittest
from core.storage import QuantumKernelStorage

class TestQuantumEngineKernel(unittest.TestCase):
    def setUp(self):
        self.kernel = QuantumKernelStorage()

    def test_write_ahead_log_generation(self):
        """Ensures transaction logs receive atomic sequence IDs."""
        tx = self.kernel.execute_transactional_write("test.metric", 100)
        self.assertEqual(tx["status"], "COMMIT_SUCCESS")
        self.assertTrue(tx["write_ahead_log_idx"] > 0)
