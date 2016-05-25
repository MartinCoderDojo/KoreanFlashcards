# coding=utf-8
import Tkinter as tk
import tkFont
import random
import time
 
class KorenFlashcards(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=300,
                          height=200)
        # Set the title
        self.master.title('Korean Flashcards')

        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()

        matrix = {}
        matrix["ga"] = '가'
        matrix["gya"] = '갸'
        matrix["geo"] = '거'
        matrix["gyeo"] = '겨'
        matrix["go"] = '고'
        matrix["gyo"] = '교'
        matrix["gu"] = '구'
        matrix["gyu"] = '규'
        matrix["geu"] = '그'
        matrix["gi"] = '기'
        matrix["gae"] = '개'


        matrix["na"] = '나'
        matrix["nya"] = '냐'
        matrix["neo"] = '너'
        matrix["nyeo"] = '녀'
        matrix["no"] = '노'
        matrix["nyo"] = '뇨'
        matrix["nu"] = '누'
        matrix["nyu"] = '뉴'
        matrix["neu"] = '느'
        matrix["ni"] = '니'
        matrix["nae"] = '내'

        matrix["da"] = '다'
        #matrix["dya"] = '댜'
        matrix["deo"] = '더'
        matrix["dyeo"] = '뎌'
        matrix["do"] = '도'
        #matrix["dyo"] = '됴'
        matrix["du"] = '두'
        matrix["dyu"] = '듀'
        matrix["deu"] = '드'
        matrix["di"] = '디'
        matrix["dae"] = '대'

        matrix["ra"] = '라'
        matrix["rya"] = '랴'
        matrix["reo"] = '러'
        matrix["ryeo"] = '려'
        matrix["ro"] = '로'
        matrix["ryo"] = '료'
        matrix["ru"] = '루'
        matrix["ryu"] = '류'
        matrix["reu"] = '르'
        matrix["ri"] = '리'
        matrix["rae"] = '래'

        matrix["ma"] = '마'
        matrix["mya"] = '먀'
        matrix["meo"] = '머'
        matrix["myeo"] = '며'
        matrix["mo"] = '모'
        matrix["myo"] = '묘'
        matrix["mu"] = '무'
        matrix["myu"] = '뮤'
        matrix["meu"] = '므'
        matrix["mi"] = '미'
        matrix["mae"] = '매'

        matrix["ba"] = '바'
        #matrix["bya"] = '뱌'
        matrix["beo"] = '버'
        matrix["byeo"] = '벼'
        matrix["bo"] = '보'
        matrix["byo"] = '뵤'
        matrix["bu"] = '부'
        matrix["byu"] = '뷰'
        matrix["beu"] = '브'
        matrix["bi"] = '비'
        matrix["bae"] = '배'

        matrix["sa"] = '사'
        matrix["sya"] = '샤'
        matrix["seo"] = '서'
        matrix["syeo"] = '셔'
        matrix["so"] = '소'
        matrix["syo"] = '쇼'
        matrix["su"] = '수'
        matrix["syu"] = '슈'
        matrix["seu"] = '스'
        matrix["si"] = '시'
        matrix["sae"] = '새'


        matrix["a"] = '아'
        matrix["ya"] = '야'
        matrix["eo"] = '어'
        matrix["yeo"] = '여'
        matrix["o"] = '오'
        matrix["yo"] = '요'
        matrix["u"] = '우'
        matrix["yu"] = '유'
        matrix["eu"] = '으'
        matrix["i"] = '이'
        matrix["ae"] = '애'

        matrix["ja"] = '자'
        matrix["jya"] = '쟈'
        matrix["jeo"] = '저'
        matrix["jyeo"] = '져'
        matrix["jo"] = '조'
        matrix["jyo"] = '죠'
        matrix["ju"] = '주'
        matrix["jyu"] = '쥬'
        matrix["jeu"] = '즈'
        matrix["ji"] = '지'
        matrix["jae"] = '재'

        # Remove gap from these characters
        matrix["cha"] = '차'
        #matrix["chya"] = '챠'
        matrix["cheo"] = '처'
        matrix["chyeo"] = '쳐'
        matrix["cho"] = '초'
        matrix["chyo"] = '쵸'
        matrix["chu"] = '추'
        matrix["chyu"] = '츄'
        matrix["cheu"] = '츠'
        matrix["chi"] = '치'
        matrix["chae"] = '채'

        matrix["ka"] = '카'
        matrix["kya"] = '캬'
        matrix["keo"] = '커'
        matrix["kyeo"] = '켜'
        matrix["ko"] = '코'
        matrix["kyo"] = '쿄'
        matrix["ku"] = '쿠'
        matrix["kyu"] = '큐'
        matrix["keu"] = '크'
        matrix["ki"] = '키'
        matrix["kae"] = '캐'

        matrix["ta"] = '타'
        #matrix["tya"] = '탸'
        matrix["teo"] = '터'
        matrix["tyeo"] = '텨'
        matrix["to"] = '토'
        #matrix["tyo"] = '툐'
        matrix["tu"] = '투'
        matrix["tyu"] = '튜'
        matrix["teu"] = '트'
        matrix["ti"] = '티'
        matrix["tae"] = '태'

        matrix["pa"] = '파'
        #matrix["pya"] = '퍄'
        matrix["peo"] = '퍼'
        matrix["pyeo"] = '펴'
        matrix["po"] = '포'
        matrix["pyo"] = '표'
        matrix["pu"] = '푸'
        matrix["pyu"] = '퓨'
        matrix["peu"] = '프'
        matrix["pi"] = '피'
        matrix["pae"] = '패'

        matrix["ha"] = '하'
        #matrix["hya"] = '햐'
        matrix["heo"] = '허'
        matrix["hyeo"] = '혀'
        matrix["ho"] = '호'
        matrix["hyo"] = '효'
        matrix["hu"] = '후'
        matrix["hyu"] = '휴'
        matrix["heu"] = '흐'
        matrix["hi"] = '히'
        matrix["hae"] = '해'

        self.matrix = matrix

        self.sylable = tk.Label(self, text=self.randomCharacter(), font=("Helvetica", 100))
        self.statement = tk.Label(self, text="Enter your answer: ")

        # The recipient text entry control and its StringVar
        self.guess_var = tk.StringVar()
        self.guess = tk.Entry(self,
                                  textvariable=self.guess_var)
        self.guess_var.set('')
 
        # The enter button
        self.enter_button = tk.Button(self,
                                   text='Enter',
                                   command=self.check)
 
        # Put the controls on the form
        self.sylable.pack(fill=tk.X, side=tk.TOP)
        self.statement.pack(fill=tk.X, side=tk.TOP)
        self.enter_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.guess.pack(fill=tk.X, side=tk.BOTTOM)
 
    def randomCharacter(self):
        self.key = random.choice(self.matrix.keys())
        return self.matrix[self.key]

    def check(self):
        if(self.guess_var.get() == self.key):
          answer = 'Correct'
        else:
          answer = 'Wrong, answer is ' + self.key

        self.statement['text'] = answer
        self.master.update()
        time.sleep(1)
        self.next()

    def next(self):
        self.statement['text'] = 'Enter your answer: '
        self.sylable['text'] = self.randomCharacter()

        
    def run(self):
        ''' Run the app '''
        self.mainloop()
 
app = KorenFlashcards(tk.Tk())
app.run()