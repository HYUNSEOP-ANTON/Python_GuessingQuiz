from tkinter import *
from tkinter import messagebox
#함수 코딩 순서) 시작 및 1번문제 - 정답체크 - 다음문제 - ... - 마지막 인터페이스
hintnum=0; score=0; m=0

def exitgame (): #게임 종료 함수
    window.destroy()
    
def about_game(): #게임 설명 함수
    messagebox.showinfo("How To Play", " 1.사진과 힌트를 사용해서 무슨 건물인지 맞춰보세요.\n 2.힌트 사용 시 최대 점수가 차감됩니다.\n 3.오탈자에 주의해주세요!\n 4.다음 문제 넘기기전 꼭 정답을 제출해주세요!")

def showhint(): #힌트 제공 함수
    global hintnum 
    global m
    hintmark[m][hintnum].config(image=building_image[m][hintnum])
    hintnum += 1
    if hintnum ==4:
        messagebox.showinfo("힌트","마지막 힌트입니다!")

 # 게임시작 및 1번 문제
def gamestart():
    game_startbutton.destroy() #첫 인터페이스 버튼 지우기
    about_game.destroy()
    game_exit.destroy()
    image_main.destroy()
    
    global image1 #첫번째 이미지 불러오기
    image1=Label(window,image=image_answer1)
    image1.place(x=130,y=200)

    hintmark[0][0].place(x=400,y=200) #힌트 이미지 불러오기
    hintmark[0][1].place(x=670,y=200)
    hintmark[0][2].place(x=940,y=200)
    hintmark[0][3].place(x=1210,y=200)

    global hintbutton #힌트버튼 배치
    hintbutton=Button(window,text="힌트",command=showhint,font=("Arial bold", 20))
    hintbutton.place(x=740,y=450)
    score_label.place(x=1250,y=100) #점수를 시작이후에 보이게 수정
    
    user_answer_entry1.place(x=720,y=600) #정답 입력칸, 제출버튼, 다음문제 버튼 배치
    submit_button1.place(x=900, y=590)
    next_1_button.place(x=1300,y=650)

def check_answer1(): # 1번 문제 정답 체크 함수
    user_answer = user_answer_entry1.get()
    if user_answer==answerlist[0]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10; next_1()
        elif hintnum ==1:
            score+=9; next_1()
        elif hintnum ==2:
            score+=8; next_1()
        elif hintnum ==3:
            score+=7; next_1()
        else:
            score+=6;next_1()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_1(): #2번 문제
    image1.destroy() 
    global m
    global hintnum
    hintnum=0
    next_1_button.destroy()
    submit_button1.destroy()
    user_answer_entry1.destroy()
    for i in range (4):
        hintmark[0][i].destroy()

    global image2
    image2=Label(window,image=image_answer2)
    image2.place(x=130,y=200) 
    next_2_button.place(x=1300,y=650)
    user_answer_entry2.place(x=720,y=600)
    submit_button2.place(x=900, y=590)
    
    hintmark[1][0].place(x=400,y=200)
    hintmark[1][1].place(x=670,y=200)
    hintmark[1][2].place(x=940,y=200)
    hintmark[1][3].place(x=1210,y=200)
    m=m+1

def check_answer2(): #2번 문제 정답 체크 함수
    user_answer = user_answer_entry2.get()
    if user_answer==answerlist[1]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_2()
        elif hintnum ==1:
            score+=9;next_2()
        elif hintnum ==2:
            score+=8;next_2()
        elif hintnum ==3:
            score+=7;next_2()
        else:
            score+=6;next_2()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")
        
def next_2(): #3번 문제
    image2.destroy()  
    global m
    global hintnum
    hintnum=0
    next_2_button.destroy()
    submit_button2.destroy()
    user_answer_entry2.destroy()
    
    for i in range (4):
        hintmark[1][i].destroy()

    global image3
    image3=Label(window,image=image_answer3)
    image3.place(x=130,y=200) 
    next_3_button.place(x=1300,y=650)
    user_answer_entry3.place(x=720,y=600)
    submit_button3.place(x=900, y=590)

    hintmark[2][0].place(x=400,y=200)
    hintmark[2][1].place(x=670,y=200)
    hintmark[2][2].place(x=940,y=200)
    hintmark[2][3].place(x=1210,y=200)
    m=m+1

def check_answer3(): #3번 문제 정답 체크 함수
    user_answer = user_answer_entry3.get()
    if user_answer==answerlist[2]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_3()
        elif hintnum ==1:
            score+=9;next_3()
        elif hintnum ==2:
            score+=8;next_3()
        elif hintnum ==3:
            score+=7;next_3()
        else:
            score+=6;next_3()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_3(): #4번 문제
    image3.destroy()    
    global m
    global hintnum
    hintnum=0
    next_3_button.destroy()
    submit_button3.destroy()
    user_answer_entry3.destroy()
    
    for i in range (4):
        hintmark[2][i].destroy()
    
    global image4
    image4=Label(window,image=image_answer4)
    image4.place(x=130,y=200) 
    next_4_button.place(x=1300,y=650)
    user_answer_entry4.place(x=720,y=600)
    submit_button4.place(x=900, y=590)

    hintmark[3][0].place(x=400,y=200)
    hintmark[3][1].place(x=670,y=200)
    hintmark[3][2].place(x=940,y=200)
    hintmark[3][3].place(x=1210,y=200)
    m=m+1

def check_answer4(): #4번 문제 정답 체크 함수
    user_answer = user_answer_entry4.get()
    if user_answer==answerlist[3]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_4()
        elif hintnum ==1:
            score+=9;next_4()
        elif hintnum ==2:
            score+=8;next_4()
        elif hintnum ==3:
            score+=7;next_4()
        else:
            score+=6;next_4()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_4(): #5번 문제
    image4.destroy()    
    global m
    global hintnum
    hintnum=0
    next_4_button.destroy()
    submit_button4.destroy()
    user_answer_entry4.destroy()
    for i in range (4):
        hintmark[3][i].destroy()
    
    global image5
    image5=Label(window,image=image_answer5)
    image5.place(x=130,y=200) 
    next_5_button.place(x=1300,y=650)
    user_answer_entry5.place(x=720,y=600)
    submit_button5.place(x=900, y=590)
    
    hintmark[4][0].place(x=400,y=200)
    hintmark[4][1].place(x=670,y=200)
    hintmark[4][2].place(x=940,y=200)
    hintmark[4][3].place(x=1210,y=200)
    m=m+1
    
def check_answer5(): #5번 문제 정답 체크 함수
    user_answer = user_answer_entry5.get()
    if user_answer==answerlist[4]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_5()
        elif hintnum ==1:
            score+=9;next_5()
        elif hintnum ==2:
            score+=8;next_5()
        elif hintnum ==3:
            score+=7;next_5()
        else:
            score+=6;next_5()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_5(): #6번 문제
    image5.destroy()   
    global m
    global hintnum
    hintnum=0
    next_5_button.destroy()
    submit_button5.destroy()
    user_answer_entry5.destroy()
    for i in range (4):
        hintmark[4][i].destroy()

    global image6
    image6=Label(window,image=image_answer6)
    image6.place(x=130,y=200) 
    next_6_button.place(x=1300,y=650)
    user_answer_entry6.place(x=720,y=600)
    submit_button6.place(x=900, y=590)
    
    hintmark[5][0].place(x=400,y=200)
    hintmark[5][1].place(x=670,y=200)
    hintmark[5][2].place(x=940,y=200)
    hintmark[5][3].place(x=1210,y=200)
    m=m+1

def check_answer6(): #6번 문제 정답 체크 함수
    user_answer = user_answer_entry6.get()
    if user_answer==answerlist[5]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_6()
        elif hintnum ==1:
            score+=9;next_6()
        elif hintnum ==2:
            score+=8;next_6()
        elif hintnum ==3:
            score+=7;next_6()
        else:
            score+=6;next_6()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")
        
def next_6(): #7번 문제
    image6.destroy()   
    global m
    global hintnum
    hintnum=0
    next_6_button.destroy()
    submit_button6.destroy()
    user_answer_entry6.destroy()
    for i in range (4):
        hintmark[5][i].destroy()

    global image7
    image7=Label(window,image=image_answer7)
    image7.place(x=130,y=200)
    next_7_button.place(x=1300,y=650)
    user_answer_entry7.place(x=720,y=600)
    submit_button7.place(x=900, y=590)
    
    hintmark[6][0].place(x=400,y=200)
    hintmark[6][1].place(x=670,y=200)
    hintmark[6][2].place(x=940,y=200)
    hintmark[6][3].place(x=1210,y=200)
    m=m+1
    
def check_answer7(): #7번 문제 정답 체크 함수
    user_answer = user_answer_entry7.get()
    if user_answer==answerlist[6]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_7()
        elif hintnum ==1:
            score+=9;next_7()
        elif hintnum ==2:
            score+=8;next_7()
        elif hintnum ==3:
            score+=7;next_7()
        else:
            score+=6;next_7()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_7(): #8번 문제
    image7.destroy()    
    global m
    global hintnum
    hintnum=0
    next_7_button.destroy()
    submit_button7.destroy()
    user_answer_entry7.destroy()
    for i in range (4):
        hintmark[6][i].destroy()

    global image8
    image8=Label(window,image=image_answer8)
    image8.place(x=130,y=200)
    next_8_button.place(x=1300,y=650)
    user_answer_entry8.place(x=720,y=600)
    submit_button8.place(x=900, y=590)
    
    hintmark[7][0].place(x=400,y=200)
    hintmark[7][1].place(x=670,y=200)
    hintmark[7][2].place(x=940,y=200)
    hintmark[7][3].place(x=1210,y=200)
    m=m+1

def check_answer8(): #8번 문제 정답 체크 함수
    user_answer = user_answer_entry8.get()
    if user_answer==answerlist[7]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_8()
        elif hintnum ==1:
            score+=9;next_8()
        elif hintnum ==2:
            score+=8;next_8()
        elif hintnum ==3:
            score+=7;next_8()
        else:
            score+=6;next_8()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_8(): #9번 문제
    image8.destroy()  
    global m
    global hintnum
    hintnum=0
    next_8_button.destroy()
    submit_button8.destroy()
    user_answer_entry8.destroy()
    for i in range (4):
        hintmark[7][i].destroy()

    global image9
    image9=Label(window,image=image_answer9)
    image9.place(x=130,y=200)
    next_9_button.place(x=1300,y=650)
    user_answer_entry9.place(x=720,y=600)
    submit_button9.place(x=900, y=590)
    
    hintmark[8][0].place(x=400,y=200)
    hintmark[8][1].place(x=670,y=200)
    hintmark[8][2].place(x=940,y=200)
    hintmark[8][3].place(x=1210,y=200)
    m=m+1

def check_answer9(): #9번 문제 정답 체크 함수
    user_answer = user_answer_entry9.get()
    if user_answer==answerlist[8]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_9()
        elif hintnum ==1:
            score+=9;next_9()
        elif hintnum ==2:
            score+=8;next_9()
        elif hintnum ==3:
            score+=7;next_9()
        else:
            score+=6;next_9()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_9(): #10번 문제
    image9.destroy()    
    global m
    global hintnum
    hintnum=0
    next_9_button.destroy()
    submit_button9.destroy()
    user_answer_entry9.destroy()
    for i in range (4):
        hintmark[8][i].destroy()

    global image10
    image10=Label(window,image=image_answer10)
    image10.place(x=130,y=200)
    user_answer_entry10.place(x=720,y=600)
    submit_button10.place(x=900, y=590)
    
    next_last_button.place(x=1300,y=650)
    
    hintmark[9][0].place(x=400,y=200)
    hintmark[9][1].place(x=670,y=200)
    hintmark[9][2].place(x=940,y=200)
    hintmark[9][3].place(x=1210,y=200)
    m=m+1
    
def check_answer10(): #10번 문제 정답 체크 함수
    user_answer = user_answer_entry10.get()
    if user_answer==answerlist[9]:
        messagebox.showinfo("정답","정답입니다.")
        global score
        global hintnum
        if hintnum == 0:
            score+=10;next_last()
        elif hintnum ==1:
            score+=9;next_last()
        elif hintnum ==2:
            score+=8;next_last()
        elif hintnum ==3:
            score+=7;next_last()
        else:
            score+=6;next_last()
        score_label.config(text="점수: {}".format(score))
    else:
        messagebox.showinfo("오답","오답입니다.")

def next_last(): #결과로 넘어가는 버튼
    image10.destroy()
    hintbutton.destroy()
    user_answer_entry10.destroy()
    submit_button10.destroy()
    next_last_button.destroy()
    
    for i in range (4):
        hintmark[9][i].destroy()

    messagebox.showinfo("END","모든 문제가 종료되었습니다.")
    result()

def result():
    image1_answer=Label(window,image=image_entire1)
    image1_answer.place(x=50,y=20)
    answer1=Label(window,text="1번:콜로세움",font=("Arial bold", 20))
    answer1.place(x=65,y=250)

    image2_answer=Label(window,image=image_entire2)
    image2_answer.place(x=370,y=20)
    answer1=Label(window,text="2번:에펠탑",font=("Arial bold", 20))
    answer1.place(x=410,y=250)

    image3_answer=Label(window,image=image_entire3)
    image3_answer.place(x=690,y=20)
    answer3=Label(window,text="3번:거북선",font=("Arial bold", 20))
    answer3.place(x=730,y=250)

    image4_answer=Label(window,image=image_entire4)
    image4_answer.place(x=1010,y=20)
    answer4=Label(window,text="4번:백악관",font=("Arial bold", 20))
    answer4.place(x=1050,y=250)

    image5_answer=Label(window,image=image_entire5)
    image5_answer.place(x=1330,y=20)
    answer5=Label(window,text="5번:키위새",font=("Arial bold", 20))
    answer5.place(x=1380,y=250)

    image6_answer=Label(window,image=image_entire6)
    image6_answer.place(x=50,y=320)
    answer6=Label(window,text="6번:비버",font=("Arial bold", 20))
    answer6.place(x=90,y=550)

    image7_answer=Label(window,image=image_entire7)
    image7_answer.place(x=370,y=320)
    answer7=Label(window,text="7번:오리너구리",font=("Arial bold", 20))
    answer7.place(x=380,y=550)

    image8_answer=Label(window,image=image_entire8)
    image8_answer.place(x=690,y=320)
    answer8=Label(window,text="8번:빅 벤",font=("Arial bold", 20))
    answer8.place(x=740,y=550)

    image9_answer=Label(window,image=image_entire9)
    image9_answer.place(x=1010,y=320)
    answer9=Label(window,text="9번:마추픽추",font=("Arial bold", 20))
    answer9.place(x=1030,y=550)

    image10_answer=Label(window,image=image_entire10)
    image10_answer.place(x=1330,y=320)
    answer10=Label(window,text="10번:성 바실리 성당",font=("Arial bold", 20))
    answer10.place(x=1310,y=550)
    

    score_label.place(x=730,y=600)
    game_exit= Button(window, text="게임 종료",font=("Arial bold", 20),command= exitgame)
    game_exit.place(x=725,y=700)

#창 띄우기
window = Tk()
window.title('사물 맞추기 게임')
window.geometry('1600x800')

main_image=PhotoImage(file="main_image.png")
image_main=Label(window,image=main_image)
image_main.pack()

#버튼 인터페이스
game_startbutton= Button(window, text='게임 시작',font=("Arial bold", 20),command=gamestart)
game_startbutton.place(x=750,y=500)
about_game=Button(window, text="게임 설명",font=("Arial bold", 20), command = about_game)
about_game.place(x=750,y=600)
game_exit= Button(window, text="게임 종료",font=("Arial bold", 20),command= exitgame)
game_exit.place(x=750,y=700)

#이미지 저장 - 건물
#콜로세움
image_answer1=PhotoImage(file="1_Colosseum\Colosseum_1.png")
images1=[PhotoImage(file="1_Colosseum\Colosseum_2.png"),
        PhotoImage(file="1_Colosseum\Colosseum_3.png"),
        PhotoImage(file="1_Colosseum\Colosseum_4.png"),
        PhotoImage(file="1_Colosseum\Colosseum_5.png")]
image_entire1=PhotoImage(file="answer_picture\Colosseum_2_entire.png")

#에펠타워
image_answer2=PhotoImage(file="2_Eiffel_Tower\Eiffel_Tower_1.png")
images2=[PhotoImage(file="2_Eiffel_Tower\Eiffel_Tower_2.png"),
        PhotoImage(file="2_Eiffel_Tower\Eiffel_Tower_3.png"),
        PhotoImage(file="2_Eiffel_Tower\Eiffel_Tower_4.png"),
        PhotoImage(file="2_Eiffel_Tower\Eiffel_Tower_5.png")]
image_entire2=PhotoImage(file="answer_picture\Eiffel_Tower_1_entire.png")

#거북선
image_answer3=PhotoImage(file="3_Turtle_ship\Turtle_ship_1.png")
images3=[PhotoImage(file="3_Turtle_ship\Turtle_ship_2.png"),
        PhotoImage(file="3_Turtle_ship\Turtle_ship_3.png"),
        PhotoImage(file="3_Turtle_ship\Turtle_ship_4.png"),
        PhotoImage(file="3_Turtle_ship\Turtle_ship_5.png")]
image_entire3=PhotoImage(file="answer_picture\Turtle_ship_1_entire.png")

#백악관
image_answer4=PhotoImage(file="4_White_house\White_house_1.png")
images4=[PhotoImage(file="4_White_house\White_house_2.png"),
        PhotoImage(file="4_White_house\White_house_3.png"),
        PhotoImage(file="4_White_house\White_house_4.png"),
        PhotoImage(file="4_White_house\White_house_5.png")]
image_entire4=PhotoImage(file="answer_picture\White_house_1_entire.png")

#키위새
image_answer5=PhotoImage(file="5_Kiwi\Kiwi_1.png")
images5=[PhotoImage(file="5_Kiwi\Kiwi_2.png"),
        PhotoImage(file="5_Kiwi\Kiwi_3.png"),
        PhotoImage(file="5_Kiwi\Kiwi_4.png"),
        PhotoImage(file="5_Kiwi\Kiwi_5.png")]
image_entire5=PhotoImage(file="answer_picture\Kiwi_1_entire.png")

#비버
image_answer6=PhotoImage(file="6_Beaver\Beaver_1.png")
images6=[PhotoImage(file="6_Beaver\Beaver_2.png"),
        PhotoImage(file="6_Beaver\Beaver_3.png"),
        PhotoImage(file="6_Beaver\Beaver_4.png"),
        PhotoImage(file="6_Beaver\Beaver_5.png")]
image_entire6=PhotoImage(file="answer_picture\Beaver_1_entire.png")

#오리너구리
image_answer7=PhotoImage(file="7_Platypus\Platypus_1.png")
images7=[PhotoImage(file="7_Platypus\Platypus_2.png"),
        PhotoImage(file="7_Platypus\Platypus_3.png"),
        PhotoImage(file="7_Platypus\Platypus_4.png"),
        PhotoImage(file="7_Platypus\Platypus_5.png")]
image_entire7=PhotoImage(file="answer_picture\Platypus_1_entire.png")

#빅벤
image_answer8=PhotoImage(file="8_Big_Ben\Big_Ben_1.png")
images8=[PhotoImage(file="8_Big_Ben\Big_Ben_2.png"),
        PhotoImage(file="8_Big_Ben\Big_Ben_3.png"),
        PhotoImage(file="8_Big_Ben\Big_Ben_4.png"),
        PhotoImage(file="8_Big_Ben\Big_Ben_5.png")]
image_entire8=PhotoImage(file="answer_picture\Big_Ben_1_entire.png")

#마추픽추
image_answer9=PhotoImage(file="9_Machu_Picchu\Machu_Picchu_1.png")
images9=[PhotoImage(file="9_Machu_Picchu\Machu_Picchu_2.png"),
        PhotoImage(file="9_Machu_Picchu\Machu_Picchu_3.png"),
        PhotoImage(file="9_Machu_Picchu\Machu_Picchu_4.png"),
        PhotoImage(file="9_Machu_Picchu\Machu_Picchu_5.png")]
image_entire9=PhotoImage(file="answer_picture\Machu_Picchu_1_entire.png")

#성 바실리 성당
image_answer10=PhotoImage(file="10_Cathedral\Cathedral_1.png")
images10=[PhotoImage(file="10_Cathedral\Cathedral_2.png"),
        PhotoImage(file="10_Cathedral\Cathedral_3.png"),
        PhotoImage(file="10_Cathedral\Cathedral_4.png"),
        PhotoImage(file="10_Cathedral\Cathedral_5.png")]
image_entire10=PhotoImage(file="answer_picture\Cathedral_1_entire.png")

#이미지 리스트화
building_image=[images1,images2,images3,images4,images5,
                images6,images7,images8,images9,images10]
#최종 이미지 넣기


#힌트 이미지 저장
hintimage=[PhotoImage(file="Hint.png")]

#힌트 이미지 리스트화
hintmark1=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark2=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark3=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark4=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark5=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark6=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark7=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark8=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark9=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
hintmark10=[Label(window,image=hintimage[0]),Label(window,image=hintimage[0]),
              Label(window,image=hintimage[0]),Label(window,image=hintimage[0])]
#힌트 이미지 리스트 - 2차원 리스트
hintmark=[hintmark1,hintmark2,hintmark3,hintmark4,hintmark5,
          hintmark6,hintmark7,hintmark8,hintmark9,hintmark10]

#정답 입력 칸
user_answer_entry1=Entry(window,width=18);user_answer_entry2=Entry(window,width=18)
user_answer_entry3=Entry(window,width=18);user_answer_entry4=Entry(window,width=18)
user_answer_entry5=Entry(window,width=18);user_answer_entry6=Entry(window,width=18)
user_answer_entry7=Entry(window,width=18);user_answer_entry8=Entry(window,width=18)
user_answer_entry9=Entry(window,width=18);user_answer_entry10=Entry(window,width=18)

#정답 리스트
answerlist=['콜로세움','에펠탑','거북선','백악관','키위새','비버','오리너구리',
            '빅 벤','마추픽추','성 바실리 성당']

#정답 체크 버튼
submit_button1=Button(window,text="정답 제출",command = check_answer1,font=("Arial bold", 20))
submit_button2=Button(window,text="정답 제출",command = check_answer2,font=("Arial bold", 20))
submit_button3=Button(window,text="정답 제출",command = check_answer3,font=("Arial bold", 20))
submit_button4=Button(window,text="정답 제출",command = check_answer4,font=("Arial bold", 20))
submit_button5=Button(window,text="정답 제출",command = check_answer5,font=("Arial bold", 20))
submit_button6=Button(window,text="정답 제출",command = check_answer6,font=("Arial bold", 20))
submit_button7=Button(window,text="정답 제출",command = check_answer7,font=("Arial bold", 20))
submit_button8=Button(window,text="정답 제출",command = check_answer8,font=("Arial bold", 20))
submit_button9=Button(window,text="정답 제출",command = check_answer9,font=("Arial bold", 20))
submit_button10=Button(window,text="정답 제출",command = check_answer10,font=("Arial bold", 20))

#다음 문제 버튼
next_1_button=Button(window,text="다음 문제",command= next_1,font=("Arial bold", 20))
next_2_button=Button(window,text="다음 문제",command= next_2,font=("Arial bold", 20))
next_3_button=Button(window,text="다음 문제",command= next_3,font=("Arial bold",20))
next_4_button=Button(window,text="다음 문제",command= next_4,font=("Arial bold",20))
next_5_button=Button(window,text="다음 문제",command= next_5,font=("Arial bold",20))
next_6_button=Button(window,text="다음 문제",command= next_6,font=("Arial bold",20))
next_7_button=Button(window,text="다음 문제",command= next_7,font=("Arial bold",20))
next_8_button=Button(window,text="다음 문제",command= next_8,font=("Arial bold",20))
next_9_button=Button(window,text="마지막 문제",command= next_9,font=("Arial bold",20))
next_last_button=Button(window,text="결과 보기",command=next_last,font=("Arial bold",20))

# 점수 제공
score_label= Label(window,text=f'점수 : {score}',font=("Arial", 25))

window.mainloop()
