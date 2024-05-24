#IdolFanClubManager
IdolFanClubManager는 아이돌 팬 클럽을 관리하는 Python 프로그램입니다. 이 프로그램은 각 아이돌의 팬 수를 추적하고, 팬 클럽 멤버들을 관리할 수 있습니다.

##설치 및 실행
저장소를 클론합니다.

bash
코드 복사
git clone https://github.com/elregansekwon/IdolFanClubManager.git
프로그램을 실행합니다.

bash
코드 복사
python main.py
##기능
각 아이돌의 팬 수를 확인할 수 있습니다.
팬 클럽 멤버를 추가하거나 제거할 수 있습니다.
각 아이돌의 팬 수를 확인할 수 있습니다.
##사용법
아이돌의 팬 수를 확인하려면 get_fan_count() 메서드를 사용합니다.

python
코드 복사
fan_count = fanclub.get_fan_count("Idol A")
print("Idol A의 팬 수:", fan_count)
팬 클럽 멤버를 추가하려면 add_member() 메서드를 사용합니다.

python
코드 복사
fanclub.add_member("Idol B", "Bob")
테스트를 실행하려면 test_fanclub.py 파일을 실행합니다.

##테스트와 Mock
이 프로젝트에서는 Unittest를 사용하여 코드를 테스트하고, Mock을 사용하여 외부 의존성을 가짜 객체로 대체합니다. Unittest는 Python의 내장 테스트 프레임워크로, 코드의 동작을 검증하는 데 사용됩니다. Mock은 테스트에서 외부 의존성을 대체하거나 모의 객체를 생성할 때 사용됩니다.

bash
코드 복사
python test_fanclub.py
##기여 방법
저장소를 포크합니다.
새로운 기능이나 버그 수정을 위한 브랜치를 만듭니다.
변경 사항을 커밋하고 푸시합니다.
Pull Request를 생성합니다.
##라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
