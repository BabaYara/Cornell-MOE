# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Test UCB1 bandit implementation.

Test that the one arm case returns the given arm as the winning arm.
Test that two-arm cases with specified random seeds return expected results.

"""
import testify as T

from moe.bandit.bla import BLA
from moe.bandit.constant import DEFAULT_BLA_SUBTYPE
from moe.tests.bandit.bandit_test_case import BanditTestCase


class BLATest(BanditTestCase):

    """Verify that different historical infos return correct results."""

    bandit_class = BLA

    def test_one_arm(self):
        """Check that the one-arm case always returns the given arm as the winning arm and the allocation is 1.0."""
        bandit = self.bandit_class(self.one_arm_test_case)
        self._test_one_arm(bandit)

    def test_two_arms_one_winner(self):
        """Check that the two-arms case with random seed 0 always allocate arm1:1.0 and arm2:0.0."""
        bandit = self.bandit_class(self.two_arms_test_case, DEFAULT_BLA_SUBTYPE, 0)
        arms_to_allocations = bandit.allocate_arms()
        T.assert_dicts_equal(arms_to_allocations, {"arm1": 1.0, "arm2": 0.0})
        T.assert_equal(bandit.choose_arm(arms_to_allocations), "arm1")

    def test_two_unsampled_arms(self):
        """Check that the two-unsampled-arms case with random seed 0 always allocate each arm equally (the allocation is 0.5 for both arms). This tests num_unsampled_arms == num_arms > 1."""
        bandit = self.bandit_class(self.two_unsampled_arms_test_case, DEFAULT_BLA_SUBTYPE, 0)
        T.assert_dicts_equal(bandit.allocate_arms(), {"arm1": 0.5, "arm2": 0.5})

if __name__ == "__main__":
    T.run()
