import sys

class Contact:#클래스가 생성되면 오브젝트가 됨, 스트링을 써서 문자열로 출력하게 함
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):#self=Contact, 문자열 출력 시 사용되는 함수
        return f"{self.name}, {self.phone}, {self.address}"#파일 작업-이름 (전화번호), 주소 저장, 덮어쓰기

class AddressBook:
    def __init__(self):#self=AdressBook
        self.contacts=[]#클래스가 생성되면 자동으로 컨택트라는 빈 배열(리스트)을 하나 생성

    def add_contact(self):
        name=input("이름을 입력하세요: ")
        phone=input("전화번호를 입력하세요: ")
        address=input("주소를 입력하세요: ")
        self.contacts.append(Contact(name, phone, address))#어팬드는 추가를 뜻함, 입력된 값을 셀프.컨택트에 추가

    def get_contact(self, searchname):
        for contact in self.contacts:
            if contact.name==searchname:
                return contact
        return None#아무것도 존재하지 않는 값으로 돌려줌, 공백도 없음

    def list_contacts(self):
        return self.contacts

    def save(self):
        self.load()
        with open("contactslist.txt", "w") as f:
            for contact in self.contacts:
                f.write(str(contact)+"\n")#9열 스트링을 부르기, 파일에 저장하기
                f.close

    def load(self):
        with open("contactslist.txt", "r") as f:#파일을 읽기 모드로 열기
            for line in f:#파일에 있는 열마다
                if len(line)>0:
                    line = line.strip()
                    print(*line.split(","))
                    contact=Contact(*line.split(","))
                    self.contacts.append(contact)
                print("파일 로딩 성공")

address_book=AddressBook()#어드래스북 클래스가 생성되는 줄->생성되면서 제일 먼저 실행되는 게 init함수
#코드는 위->아래, 오른쪽->왼쪽 : 생성된 클래스를 address_book에 넣음

while True:
    print("1. 연락처 추가")
    print("2. 연락처 조회")
    print("3. 연락처 목록")
    print("4. 연락처 저장")
    print("5. 연락처 로딩")
    print("0. 종료")
    
    choice = input("메뉴를 선택하세요: ")#입력할 수 있게 해주는 함수, 입력된 값은 choice 변수에 저장

    if choice=="1":
        address_book.add_contact()
    elif choice=="2":
        searchname=input("조회할 연락처 이름을 입력하세요: ")#입력된 값을 searchname에 저장
        contact=address_book.get_contact(searchname)#23번줄을 실행해서 돌아온 searchname값을 컨택트에 저장
        if contact:#23번줄 내용
            print(contact)
        else:
            print("해당 이름의 연락처가 없습니다.")
    elif choice=="3":
        for contact in address_book.contacts:
            print(contact)
    elif choice=="4":#연락처 저장
        address_book.save()
    elif choice=="5":
        address_book.load()
    elif choice=="0":
        sys.exit()
    else:
        print("잘못된 입력입니다.")