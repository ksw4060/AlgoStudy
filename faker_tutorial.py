from faker import Faker

faker = Faker()

print(faker.name())
print(faker.first_name())
# print(faker.last_name())
# print(faker.word())
print(faker.sentence())
print(faker.text())

"""
비밀번호 생성 -> faker.word()
게시글의 제목 -> faker.sentence()
게시글의 내용 -> faker.text()
"""
# first_name = faker.first_name()
# last_name = faker.last_name()
# email = f"{last_name}@{faker.domain_name()}"
# print(first_name)
# print(last_name)
# print(email)

# class ArticleReadTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.faker = Faker()
#         cls.articles = []
#         cls.rnd_email = f"{cls.faker.last_name()}@{cls.faker.domain_name()}"
#         for i in range(10):
#             cls.user = User.objects.create_user(cls.rnd_email, cls.faker.first_name(), cls.faker.last_name(), cls.faker.word())
#             print(cls.user)
#             # ('test@kakao.com','tester', 'testuser','popk1214')
