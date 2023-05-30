import unittest
from baham_web.models import UserProfile, Vehicle, Contract

class UserProfileConstraintsTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserProfile()

    def test_one_vehicle_per_owner(self):
        # Create two vehicles for the same owner
        vehicle1 = Vehicle(owner=self.user)
        vehicle2 = Vehicle(owner=self.user)
        self.assertTrue(vehicle1.owner == self.user)
        self.assertIsNone(vehicle2.owner)

    def test_passenger_capacity(self):
        vehicle = Vehicle(capacity=4)
        self.assertTrue(vehicle.passenger_capacity >= 0)

        # Attempt to add more passengers than the vehicle's capacity
        vehicle.add_passenger(self.user)
        vehicle.add_passenger(UserProfile())
        vehicle.add_passenger(UserProfile())
        vehicle.add_passenger(UserProfile())
        vehicle.add_passenger(UserProfile())

        self.assertEqual(len(vehicle.passengers), vehicle.passenger_capacity)

    def test_total_share(self):
        contract = Contract(share=50)
        self.assertTrue(contract.share >= 0 and contract.share <= 100)

    def test_multiple_contracts_for_companion(self):
        companion = UserProfile()
        contract1 = Contract(companion=companion)
        contract2 = Contract(companion=companion)

        self.assertIsNone(contract2.id)

if __name__ == '__main__':
    unittest.main()
