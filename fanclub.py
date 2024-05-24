class FanClub:
    def __init__(self):
        # 팬클럽 멤버 저장 딕셔너리
        # key: 아이돌 이름
        # value: 해당 아이돌의 팬 리스트
        self.members = {}

    def add_member(self, idol, member_name):
        # 특정 아이돌의 팬 추가 메서드
        # idol: 아이돌의 이름 (문자열)
        # member_name: 팬의 이름 (문자열)

        # 아이돌이 members 딕셔너리에 없으면, 새로운 리스트를 생성
        if idol not in self.members:
            self.members[idol] = []

        # 아이돌의 팬 리스트에 팬의 이름을 추가
        self.members[idol].append(member_name)

    def get_fan_count(self, idol):
        # 특정 아이돌의 팬 수를 반환 메서드
        # idol: 아이돌의 이름 (문자열)
        # 반환값: 해당 아이돌의 팬 수 (정수)

        # 아이돌이 members 딕셔너리에 있으면 팬 리스트의 길이를 반환
        if idol in self.members:
            return len(self.members[idol])

        # 아이돌이 members 딕셔너리에 없으면 0을 반환
        return 0

    def get_members(self, idol):
        # 특정 아이돌의 팬 리스트를 반환 메서드
        # idol: 아이돌의 이름 (문자열)
        # 반환값: 해당 아이돌의 팬 리스트 (리스트)

        # 아이돌이 members 딕셔너리에 있으면 팬 리스트를 반환
        if idol in self.members:
            return self.members[idol]

        # 아이돌이 members 딕셔너리에 없으면 빈 리스트를 반환
        return []
