# test_fanclub_with_mock.py

import unittest
from unittest.mock import patch
from fanclub import FanClub


class TestFanClubWithMock(unittest.TestCase):
    def setUp(self):
        # 테스트 전에 실행될 초기 설정, FanClub 인스턴스 생성
        self.fanclub = FanClub()

    @patch('fanclub.FanClub.get_fan_count')
    def test_get_fan_count_with_mock(self, mock_get_fan_count):
        # get_fan_count 메서드를 모의(mock) 객체로 대체
        # mock_get_fan_count: 모의 객체

        # 모의 객체의 반환 값을 100으로 설정
        mock_get_fan_count.return_value = 100

        # get_fan_count 호출 시 모의 객체가 반환하는 값이 100인지 확인
        self.assertEqual(self.fanclub.get_fan_count("Idol A"), 100)


if __name__ == '__main__':
    unittest.main()

# unittest
# unittest는 파이썬의 표준 테스트 라이브러리로, 코드의 일부분을 테스트하고 예상된 동작을 확인하는 데 사용
# 테스트 케이스를 작성할 때 주로 사용되며, 각 테스트 케이스는 unittest.TestCase 클래스를 상속받음
# 각 테스트 케이스는 테스트를 설정하는 setUp 메서드와 테스트를 정의하는 메서드로 구성
# 테스트를 실행하려면 unittest.main()을 호출하거나 IDE에서 실행

# mock
# 모의 객체
# 테스트 중에 다른 객체를 대신하여 사용되는 가짜 객체
# 테스트 중에 특정 메서드의 호출을 가로채고, 반환 값을 조작하거나 사이드 이펙트를 감지 가능

# unittest를 사용하여 코드의 일부분을 테스트하고, mock을 사용하여 외부 의존성을 가진 코드를 테스트