from faker import Faker

faker = Faker("ko_KR")

print(faker.name())
print(faker.first_name())
print(faker.last_name())
print(faker.word())
print(faker.sentence())
print(faker.text())

"""
비밀번호 생성 -> word
게시글의 제목 -> sentence
게시글의 내용 -> text
"""
