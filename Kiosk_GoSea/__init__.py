#공유 변수, 함수들
class catalog: #메뉴, 가격 정보 저장
    def __init__(self):
        self.menu = [] # menulist
        self.price = [] #pricelist
class receipt: #영수증(장바구니) 정보 저장
    def __init__(self):
        self.take = '' #take in, take out
        self.category = [] #save category
        self.menu = [] #save menu
        self.op = [] #save option
        self.price = [] #save price
        self.menuop = []

    def print_reciept(self,num): #영수증 출력
        print('<김밥천국 주문서>')
        print(f'주문번호:{num}')
        print(f'이용방법:{self.take}')
        print('카테고리)메뉴',' '*6,'금액',' '*6,'옵션')
        print('-'*70)
        for i in range(len(self.menu)):
            print(f'{self.category[i]}){self.menu[i]:<10}{self.price[i]:<10}{self.menuop[i]}')
        print('-' * 70)
        print(f'합 계:{self.totalprice()}원')

    def sel_op(self,ind): #옵션별 가격 적용
        self.price[-1] += op_price[ind]

    def totalprice(self): #총 가격 계산
        if len(self.price) == 0: return 0
        sum = 0
        for k in range(len(self.menu)):
            sum += self.price[k]
        return sum

    def clearAll(self): #장바구니 정보 초기화
        self.take = ''
        self.category = []
        self.menu = []
        self.op = []
        self.price = []
        self.menuop = []


op_list = ['밥 추가','콜라 추가','사이다 추가','환타 추가'] #옵션 정보
op_price=[1000,2000,2000,2000]
cate_list = ['김밥류','분식류','식사류'] #카테고리 정보
#카테고리 별 메뉴 정보
cate1 = catalog()
cate1.menu = ['원조 김밥','참치 김밥','돈까스 김밥']
cate1.price = [2500,3500,4000]
cate2 = catalog()
cate2.menu = ['라면','우동','떡볶이','만두']
cate2.price = [3500,4500,4500,4000]
cate3 = catalog()
cate3.menu = ['제육덮밥','돈까스','비빔밥','김치찌개']
cate3.price = [7000,7000,6500,6500]

catelist = [cate1,cate2,cate3] #base menu
#장바구니
shopcart = receipt()
#회원 정보
memlist={'홍길동':0}
phonelist=['12341234']
#매출 정보 (총, 카테고리별)
t_income=[]
c_income=[0]*len(cate_list)