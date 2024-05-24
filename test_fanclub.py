import unittest
from fanclub import FanClub


class TestFanClub(unittest.TestCase):
    def setUp(self):
        # 테스트 전에 실행될 초기 설정, FanClub 인스턴스 생성
        self.fanclub = FanClub()

    def test_add_member(self):
        # 팬 추가 테스트
        self.fanclub.add_member("Idol A", "Alice")
        self.fanclub.add_member("Idol A", "Bob")

        # 팬 추가 확인
        self.assertIn("Alice", self.fanclub.get_members("Idol A"))
        self.assertIn("Bob", self.fanclub.get_members("Idol A"))

    def test_get_fan_count(self):
        # 팬 추가
        self.fanclub.add_member("Idol B", "Charlie")
        self.fanclub.add_member("Idol B", "Dave")

        # 팬 수 확인
        self.assertEqual(self.fanclub.get_fan_count("Idol B"), 2)
        self.assertEqual(self.fanclub.get_fan_count("Idol C"), 0)

    def test_get_members(self):
        # 팬 추가
        self.fanclub.add_member("Idol D", "Eve")
        self.fanclub.add_member("Idol D", "Frank")

        # 팬 목록 확인
        members = self.fanclub.get_members("Idol D")
        self.assertEqual(members, ["Eve", "Frank"])
        self.assertEqual(self.fanclub.get_members("Idol E"), [])


if __name__ == '__main__':
    unittest.main()
