from lib2to3.pygram import python_grammar_no_print_statement
from tkinter import W
import pygame
import random
import time
import math

pygame.init()
green_pixels_xlist=[0]
green_pixels_ylist=[0]
turn=1
width=1000
life1=100
life2=100
last_x=0
last_y=0
length=800
number_of_special1=2
number_of_special2=2
x_tank1=20
y_tank1=680
x_tank2=930
y_tank2=680
bullet_x2=1
bullet_y2=1
bullet_x1=1
bullet_y1=1
fuel1=40
fuel2=40
angle2=1
angle1=1
explosion_img=pygame.image.load('D:\Practica\Resurse_Joc\explozie.png')
window=pygame.display.set_mode((width,length))
pygame.display.set_caption("Tanks")
bg_img=pygame.image.load('D:\Practica\Resurse_Joc\harta.png')
bg_img=pygame.transform.scale(bg_img,(width,length))
tank1_img=pygame.image.load('D:\Practica\Resurse_Joc\h_tank1.png')
tank1_img=pygame.transform.scale(tank1_img,(60,40))
tank2_img=pygame.image.load('D:\Practica\Resurse_Joc\h_tank2.png')
tank2_img=pygame.transform.scale(tank2_img,(60,40))
icon=pygame.image.load('D:\Practica\Resurse_Joc\icon.png')
pygame.display.set_icon(icon)
bullet2_img=pygame.image.load('D:\Practica\Resurse_Joc\h_glont.png')
bullet2_img=pygame.transform.scale(bullet2_img,(60,40))
bullet1_img=pygame.image.load('D:\Practica\Resurse_joc\h_glont.png')
bullet1_img=pygame.transform.scale(bullet1_img,(60,40))
crash_sound = pygame.mixer.Sound('D:\Practica\Resurse_joc\h_explozie.wav')
win_sound=pygame.mixer.Sound('D:\Practica\Resurse_joc\win.wav')
shot_sound=pygame.mixer.Sound('D:\Practica\Resurse_joc\h_shot.wav')
little_bullet_img=pygame.image.load('D:\Practica\Resurse_joc\h_red_bullet.png')
little_bullet_img=pygame.transform.scale(little_bullet_img,(60,40))	
spacePressed=False
M_Pressed=False
special1=False
special2=False
small_proj1=False
small_proj2=False
speed1=47
speed2=47
end_window=False
font = pygame.font.Font('freesansbold.ttf', 17)
#update power on map
def update_speed2(speed2):

	text_speed2 = font.render(":Power", True, (255,0,0), (15,135,255))
	textRectspeed2 = text_speed2.get_rect()
	textRectspeed2.center = (900, 50)
	window.blit(text_speed2,textRectspeed2)
	
	if speed2==49.5:
		pygame.draw.rect(window,(255,0,0),(815,43,50,10))
	if speed2==47:
		pygame.draw.rect(window,(255,0,0),(815,43,0,10))
	if speed2==47.5:
		pygame.draw.rect(window,(255,0,0),(815,43,10,10))
	if speed2==48:
		pygame.draw.rect(window,(255,0,0),(815,43,20,10))
	if speed2==48.5:
		pygame.draw.rect(window,(255,0,0),(815,43,30,10))
	if speed2==49:
		pygame.draw.rect(window,(255,0,0),(815,43,40,10))
def update_speed1(speed1):
	
	text_speed1=font.render("Power:",True,(255,0,0),(15,135,255))
	textRectspeed1=text_speed1.get_rect()
	textRectspeed1.center=(50,50)
	window.blit(text_speed1,textRectspeed1)
	if speed1==49.5:
		pygame.draw.rect(window,(255,0,0),(80,46,50,10))
	if speed1==47:
		pygame.draw.rect(window,(255,0,0),(80,46,0,10))
	if speed1==47.5:
		pygame.draw.rect(window,(255,0,0),(80,46,10,10))
	if speed1==48:
		pygame.draw.rect(window,(255,0,0),(80,46,20,10))
	if speed1==48.5:
		pygame.draw.rect(window,(255,0,0),(80,46,30,10))
	if speed1==49:
		pygame.draw.rect(window,(255,0,0),(80,46,40,10))
#update map text
def update_angle1(angle1):
		text_angle1=font.render("Angle:"+str((angle1)),True,(255,0,0),(15,135,255))
		textRectangle1=text_angle1.get_rect()
		textRectangle1.center=(50,67)
		window.blit(text_angle1,textRectangle1)
def update_angle2(angle2):
		text_angle2=font.render("Angle:"+str((angle2)),True,(255,0,0),(15,135,255))
		textRectangle2=text_angle2.get_rect()
		textRectangle2.center=(900,67)
		window.blit(text_angle2,textRectangle2)
def update_fuel1(fuel1):
	text_fuel1=font.render("Fuel:"+str(fuel1),True,(255,0,0),(15,135,255))
	textRectfuel1=text_fuel1.get_rect()
	textRectfuel1.center=(900,84)
	window.blit(text_fuel1,textRectfuel1)
def update_fuel2(fuel2):
	text_fuel2=font.render("Fuel:"+str(fuel2),True,(255,0,0),(15,135,255))
	textRectfuel2=text_fuel2.get_rect()
	textRectfuel2.center=(50,84)
	window.blit(text_fuel2,textRectfuel2)
def update_life1(life1):
	text_life1=font.render("Life:"+str(life1),True,(255,0,0),(15,135,255))
	textRectlife1=text_life1.get_rect()
	textRectlife1.center=(50,101)
	window.blit(text_life1,textRectlife1)
def update_life2(life2):
	text_life2=font.render("Life:"+str(life2),True,(255,0,0),(15,135,255))
	textRectlife2=text_life2.get_rect()
	textRectlife2.center=(900,101)
	window.blit(text_life2,textRectlife2)

def showmap(angle1,speed1,angle2,speed2,is_explosion1,is_explosion2,small_proj1,small_proj2):
       #desenare mapa
	window.fill((0,0,0))
	window.blit(bg_img,(0,0))
	window.blit(tank1_img,(x_tank1,y_tank1))
	window.blit(tank2_img,(x_tank2,y_tank2))
	update_speed1(speed1)
	update_speed2(speed2)
	update_angle1(angle1)
	update_angle2(angle2)
	update_fuel1(fuel1)
	update_fuel2(fuel2)
	update_life1(life1)
	update_life2(life2)
	pygame.draw.rect(window, (0,250,0), pygame.Rect(0, 720, 1000, 80))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(100,710,740,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(140,700,640,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(180,690,560,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(220,680,490,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(280,670,400,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(310,660,330,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(350,650,250,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(380,640,200,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(440,630,80,10))
	pygame.draw.rect(window,(0,250,0),pygame.Rect(470,620,20,10))
	for i in range(len(green_pixels_ylist)):
		if green_pixels_xlist[i]!=0 and green_pixels_ylist[i]!=0:
			pygame.draw.rect(window,(15,135,255),pygame.Rect(green_pixels_xlist[i]+5,green_pixels_ylist[i],45,45))
	
	window.blit(tank1_img,(x_tank1,y_tank1))
	window.blit(tank2_img,(x_tank2,y_tank2))
	if small_proj1==False:
		window.blit(bullet1_img,(bullet_x1,bullet_y1))
	else:   #schimbare proiectil in cazul celui special
		window.blit(little_bullet_img,(bullet_x1,bullet_y1))
	if small_proj2==False:
		window.blit(bullet2_img,(bullet_x2,bullet_y2))
	else:
		window.blit(little_bullet_img,(bullet_x2,bullet_y2))
	if is_explosion2:
		window.blit(explosion_img,(x_tank2,y_tank2-20))
		pygame.time.delay(100)
		is_explosion2=False #afisare animatie explozie
	if is_explosion1:
		window.blit(explosion_img,(x_tank1,y_tank1-20))
		pygame.time.delay(100)
		is_explosion1=False

	#vector de pixeli prin care trece ghiuleaua
	#verificat si scosi de fiecare data din harta

#verificat coliziune cu harta
def collision(bullet_x,bullet_y):
	color=window.get_at((int(bullet_x),int(bullet_y)))
	if(color==(0,250,0,255)):
		return True
	return False
def tank_boom(bullet_x,bullet_y,last_x,last_y,tank_number,x_tank,y_tank,tip=0): 
	
	if tip==1:
		if tank_number==1:
			if last_x>=x_tank and last_x<=x_tank+35 and last_y<=y_tank+15 and bullet_x>=x_tank and bullet_y>=y_tank:
				bullet_x=last_x
				bullet_y=last_y
				return True
		if tank_number==2:
			if last_x<=x_tank+35 and last_x>=x_tank and last_y<=y_tank+15 and bullet_y>=y_tank and bullet_x<=x_tank:
				bullet_x=last_x
				bullet_y=last_y
				return True
		return False
	else:	                                                         
		if tank_number==1:
			if last_x<=x_tank and last_y<=y_tank+15 and bullet_x>=x_tank and bullet_y>=y_tank:
				bullet_x=last_x 
				bullet_y=last_y  # numerele 25 reprezinta eroarea data de inaltimea tank-ului(in pixeli)                
				 #numerele 15 reprezinta inaltimea fata de tank unde explodeaza proiectilul, va exploda la o distanta convenabila
				return True
		if tank_number==2:

			if last_x>=x_tank and last_y<=y_tank+15 and bullet_x<=x_tank and bullet_y>=y_tank:
				bullet_x=last_x
				bullet_y=last_y
				return True	
	return False

def tank_go_up1(x,y):
	color=window.get_at((x-5,y+30))#verificare daca este o singura bucata de zid(poate urca)
	color_up=window.get_at((x-5,y+25)) 
	if color==(0,250,0,255) and color_up!=(0,250,0,255):
		return True
	return False

def tank_go_up2(x,y):
	color=window.get_at((x+10,y+30))  #verificare daca este o singura bucata de zid
	color1=window.get_at((x+10,y+25)) #verificare daca sunt 2 bucati de zid
	if color==(0,250,0,255) and color1!=(0,250,0,255):
		return True
	return False

def tank_go_down(x,y):
	#pentru tankul 1 verific de la pozitia initiala x_tank1+15 pentru ca de acolo incepe desenul"adevarat" al tankului
	is_on_side=True
	for i in range(30):
		if window.get_at((x+15+i,y+41))!=(15,135,255,255):
			is_on_side=False
	return is_on_side

def can_shoot():
	if M_Pressed==False and spacePressed==False and special1==False and special2==False and small_proj1==False and small_proj2==False:
		return True
	return False

#inscrisurile din meniul initial
red=(255,0,0)
menu_img=pygame.image.load('D:\Practica\Resurse_Joc\h_tank_background1.jpg')
menu_img=pygame.transform.scale(menu_img,(width,length))
menu_window=pygame.display.set_mode((width,length))
font1 = pygame.font.Font('freesansbold.ttf', 40)
text1 = font1.render('Welcome to Tanks Game', True, red, (255,255,255))
textRect1 = text1.get_rect()
textRect1.center = (width//2, 100)


font2=pygame.font.Font('freesansbold.ttf',20)
text2=font2.render('Control:',True,red,(255,255,255))
textRect2=text2.get_rect()
textRect2.center=(width//2-200,150)

font3=pygame.font.Font('freesansbold.ttf',20)
text3=font3.render('TAB-Start the Game',True,red,(255,255,255))
textRect3=text3.get_rect()
textRect3.center=(width//2-100,200)

font4=pygame.font.Font('freesansbold.ttf',20)
text4=font4.render('A,D for tank1 move and Left,Right Keys for tank2 move',True,red,(255,255,255))
textRect4=text4.get_rect()
textRect4.center=(width//2-100,250)

font5=pygame.font.Font('freesansbold.ttf',20)
text5=font5.render('W,S for tank1 change angle and Up,Down for tank2 angle',True,red,(255,255,255))
textRect5=text5.get_rect()
textRect5.center=(width//2-100,300)

font6=pygame.font.Font('freesansbold.ttf',20)
text6=font6.render('M for shoot(tank1),Space for shoot(tank2)',True,red,(255,255,255))
textRect6=text6.get_rect()
textRect6.center=(width//2-100,350)

font7=pygame.font.Font('freesansbold.ttf',20)
text7=font7.render('Q and Z for increase and decrease power(tank1),P and L for tank2\n',True,red,(255,255,255))
textRect7=text7.get_rect()
textRect7.center=(width//2-100,400)

font10=pygame.font.Font('freesansbold.ttf',20)
text10=font10.render('1 and I for special power(projectile follows the tank)',True,red,(255,255,255))
textRect10=text10.get_rect()
textRect10.center=(width//2-100,450)

font11=pygame.font.Font('freesansbold.ttf',20)
text11=font11.render('2 and U for special power(little projectile, big power)- 2 projectiles',True,red,(255,255,255))
textRect11=text11.get_rect()
textRect11.center=(width//2-100,500)

font8=pygame.font.Font('freesansbold.ttf',60)
text8=font8.render('Red Tank Wins!',True,red,(255,255,255))
textRect8=text8.get_rect()
textRect8.center=(width//2,length//2)

font9=pygame.font.Font('freesansbold.ttf',60)
text9=font9.render('Green Tank Wins!',True,(0,255,0),(255,255,255))
textRect9=text9.get_rect()
textRect9.center=(width//2,length//2)



#meniul initial
run_menu=True
running=False
while run_menu:
	menu_window.blit(menu_img,(0,0))
	menu_window.blit(text1,textRect1)
	menu_window.blit(text2,textRect2)
	menu_window.blit(text3,textRect3)
	menu_window.blit(text4,textRect4)
	menu_window.blit(text5,textRect5)
	menu_window.blit(text6,textRect6)
	menu_window.blit(text7,textRect7)
	menu_window.blit(text10,textRect10)
	menu_window.blit(text11,textRect11)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run_menu=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_TAB:
				running=True
				run_menu=False
	pygame.display.update()

			
while running:
	
	pygame.time.delay(50)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
			#miscarea tank-ului, schimbarea unghiului, a puterii, respectiv initializarea coordonatelor proiectilului
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_BACKSPACE:
				running=False
			if event.key==pygame.K_q:
				if speed1<49.5:
					speed1=speed1+0.5
			if event.key==pygame.K_z:
				if speed1>47:
					speed1=speed1-0.5
			if event.key==pygame.K_p:
				if speed2<49.5:
					speed2=speed2+0.5
			if event.key==pygame.K_l:
				if speed2>47:
					speed2=speed2-0.5
			if event.key==pygame.K_d:
			
				if fuel2>0:
					x_tank1=x_tank1+5
					if x_tank1>930:
						x_tank1=x_tank1-5
						fuel2=fuel2+1
					fuel2=fuel2-1

			if event.key==pygame.K_a:
				if fuel2>0:
					x_tank1=x_tank1-5
					if x_tank1<10:
						x_tank1=x_tank1+5
						fuel2=fuel2+1
					fuel2=fuel2-1

			if event.key==pygame.K_RIGHT:
				if fuel1>0:
					x_tank2=x_tank2+5
					if x_tank2>930:
						x_tank2=x_tank2-5
						fuel1=fuel1+1
					fuel1=fuel1-1
			if event.key==pygame.K_LEFT:
				if fuel1>0:
					x_tank2=x_tank2-5
					if x_tank2<0:
						x_tank2=x_tank2+5
						fuel1=fuel1+1
					fuel1=fuel1-1
			if event.key==pygame.K_SPACE:
				if can_shoot() and turn==2:
					spacePressed=True
					gravity = 9.81 
					velocity = -speed2
					vx = velocity * math.cos(math.radians(angle2))
					vy = velocity * math.sin(math.radians(angle2))
					dt = 0.08
					pygame.mixer.Sound.play(shot_sound)
					pygame.mixer.music.stop()
					bullet_x2=x_tank2-10 #initializare proiectil
					bullet_y2=y_tank2
					turn=1
			if event.key==pygame.K_m:
				if can_shoot() and turn==1:
					gravity = 9.81
					velocity = speed1
					vx = velocity * math.cos(math.radians(angle1))
					vy = velocity * math.sin(math.radians(angle1))
					dt = 0.08
					pygame.mixer.Sound.play(shot_sound)
					pygame.mixer.music.stop()
					M_Pressed=True
					bullet_x1=x_tank1
					bullet_y1=y_tank1
					turn=2
			if event.key==pygame.K_1:
				if can_shoot() and turn==1:
					special1=True
					pygame.mixer.Sound.play(shot_sound)
					pygame.mixer.music.stop()
					bullet_x1=x_tank1+10
					bullet_y1=y_tank1
					turn=2
			if event.key==pygame.K_i:
				if can_shoot() and turn==2:
					special2=True
					pygame.mixer.Sound.play(shot_sound)
					pygame.mixer.music.stop()
					bullet_x2=x_tank2-10
					bullet_y2=y_tank2
					turn=1
			if event.key==pygame.K_2:
				if can_shoot() and number_of_special1>0 and turn==1:
					small_proj1=True
					gravity = 9.81
					velocity = speed1
					vx = velocity * math.cos(math.radians(angle1))
					vy = velocity * math.sin(math.radians(angle1))
					dt = 0.08
					pygame.mixer.Sound.play(shot_sound)
					pygame.mixer.music.stop()
					bullet_x1=x_tank1+10
					bullet_y1=y_tank1
					number_of_special1=number_of_special1-1
					turn=2
			if event.key==pygame.K_u:
				if can_shoot() and number_of_special2>0 and turn==2:
					small_proj2=True
					gravity = 9.81
					velocity = -speed2
					vx = velocity * math.cos(math.radians(angle2))
					vy = velocity * math.sin(math.radians(angle2))
					dt = 0.08
					pygame.mixer.Sound.play(shot_sound)
					pygame.mixer.music.stop()
					small_proj2=True
					bullet_x2=x_tank2-10
					bullet_y2=y_tank2
					number_of_special2=number_of_special2-1
					turn=1
		
				
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
						if angle2 <89:
							angle2=angle2+1

				if event.key==pygame.K_DOWN:
					if angle2>0:
						angle2=angle2-1
				if event.key==pygame.K_w:
					if angle1<89:
						angle1=angle1+1
				if event.key==pygame.K_s:
					if angle1>0:
						angle1=angle1-1
	#deplasare proiectil emis de tankul 1 in functie de putere(speed) si unghi
	if bullet_x1>=970:  #iesire din mapa si "oprire activitate"
		bullet_x1=bullet_x1+1000
		M_Pressed=False
		special1=False
		small_proj1=False
	if bullet_y1 >=790 or bullet_y2>=790:
		bullet_y1=bullet_y1+1000
		M_Pressed=spacePressed=False
		special1=special2=False
		small_proj1=small_proj2=False
	
	if bullet_x2<=9:  # verificare iesire din mapa
			bullet_x2=bullet_x2-1000  #iesire din mapa pentru a disparea proiectilul si "oprire activitate"
			spacePressed=False
			special2=False
			small_proj2=False

	if M_Pressed or small_proj1:
		last_x=bullet_x1
		last_y=bullet_y1
		bullet_x1=bullet_x1+vx*dt*1.8   #ecuatia miscarii proiectilului
		bullet_y1=bullet_y1-vy*dt
		vy=vy-0.5*gravity*dt
		dt=dt+0.01
	if spacePressed or small_proj2:
		last_x=bullet_x2
		last_y=bullet_y2
		bullet_x2=bullet_x2+vx*dt*1.8  #ecuatia miscarii proiectilului
		bullet_y2=bullet_y2+vy*dt
		vy=vy+0.5*gravity*dt
		dt=dt+0.01
	
		
		
	if special1:
		 #atunci cand este activata puterea speciala 1, proiectilul "va cadea" peste tank
		if bullet_x1<=width//2:

			bullet_x1=bullet_x1+10
			bullet_y1=bullet_y1-10
		else:
			bullet_x1=bullet_x1+10
			bullet_y1=bullet_y1+3
			if abs(bullet_x1-x_tank2)<=40:   #verificarea apropierii
				bullet_x1=x_tank2
			if abs(bullet_y1-y_tank2)<=40:
				bullet_y1=y_tank2

	if special2:
		# atunci cand este activata puterea speciala a tankului 2, proiectilul "va cadea" peste tank
		if bullet_x2>=width//2:
			bullet_x2=bullet_x2-10
			bullet_y2=bullet_y2-10
		else:
			bullet_x2=bullet_x2-10
			bullet_y2=bullet_y2+5
			if abs(bullet_x2-x_tank1)<=40:  #verificarea apropierii
				bullet_x2=x_tank1
			if abs(bullet_y2-y_tank1)<=40:
				bullet_y2=y_tank1
	
	
			 #iesire din mapa
	is_explosion1=False  #variabile care verifica daca este explozie, folosite pentru afisarea animatiei pentru explozie
	is_explosion2=False
	if  (tank_boom(bullet_x1,bullet_y1,last_x,last_y,1,x_tank2,y_tank2,0)==True and small_proj1==False):
		pygame.mixer.Sound.play(crash_sound)
		pygame.mixer.music.stop()
		if special1==True:
			life2=life2-10
		else:
			life2=life2-20
		bullet_x1=10000
		last_x=bullet_x1+1
		bullet_y1=bullet_y1-1000    #verificare coliziune fara proiectil special
		last_y=bullet_y1
		is_explosion2=True
		M_Pressed=False
		spacePressed=False
		special1=False
  
	if  (tank_boom(bullet_x2,bullet_y2,last_x,last_y,2,x_tank1,y_tank1,0)==True and small_proj2==False):
		pygame.mixer.Sound.play(crash_sound)
		pygame.mixer.music.stop()
		if special2==True:
			life1=life1-10
		else:
			life1=life1-20
		bullet_x2=bullet_x2+10000
		last_x=bullet_x2-1
		bullet_y2=bullet_y2-1000    #verificare coliziune fara proiectil special
		last_y=bullet_y2
		is_explosion1=True
		spacePressed=False
		special2=False
	if  (M_Pressed==True or special1==True or small_proj1==True) and bullet_x1<=970 :
		if collision(int(bullet_x1+20),int(bullet_y1+20))==True:
			M_Pressed=False
			special1=False 
			small_proj1=False #dezactivarea variabilelor care dau tragerea
			green_pixels_xlist.append(int(bullet_x1))
			green_pixels_ylist.append(int(bullet_y1))  #adaugare in vectorul de coordonate pentru a forma cratere
			bullet_x1=10000
			last_x=bullet_x1+1
			bullet_y1=bullet_y1-1000
			last_y=bullet_y1 #iesire din mapa
	# verificarea coliziunii proiectilului 2 cu bucatile de pamant
	if (spacePressed or special2 or small_proj2) ==True and bullet_x2>=30:
		if collision(int(bullet_x2+20),int(bullet_y2+20))==True:
			spacePressed=False
			special2=False  
			small_proj2=False #dezactivarea variabilelor care dau tragerea
			green_pixels_xlist.append(bullet_x2)
			green_pixels_ylist.append(bullet_y2)
			bullet_x2=10000
			last_x=bullet_x2-1
			bullet_y2=bullet_y2-1000
			last_y=bullet_y2
 # verificarea coliziunii atunci cand se trimit proiectile cu damage mare
	if small_proj1==True:
		if tank_boom(bullet_x1,bullet_y1,last_x,last_y,1,x_tank2,y_tank2,1):
			pygame.mixer.Sound.play(crash_sound)
			pygame.mixer.music.stop()
			life2=life2-40
			bullet_x1=10000
			last_x=bullet_x1-1
			bullet_y1=bullet_y1-1000
			last_y=bullet_y1
			is_explosion2=True
			small_proj1=False
   
	if small_proj2==True:
		if tank_boom(bullet_x2,bullet_y2,last_x,last_y,2,x_tank1,y_tank1,1):
			pygame.mixer.Sound.play(crash_sound)
			pygame.mixer.music.stop()
			life1=life1-40
			bullet_x2=10000
			last_x=bullet_x2+1
			bullet_y2=bullet_y2-1000
			last_y=bullet_y2
			is_explosion1=True
			small_proj2=False
	# in liniile urmatoare se realizeaza caderea sau urcarea tank-urilor atunci cand trec prin zone specifice acestor actiuni
	if tank_go_up1(x_tank1+50,y_tank1):
		x_tank1=x_tank1+5
		y_tank1=y_tank1-10 
	if tank_go_up2(x_tank2,y_tank2):
		x_tank2=x_tank2-5
		y_tank2=y_tank2-10
	if tank_go_down(x_tank1,y_tank1):
		x_tank1=x_tank1-1
		y_tank1=y_tank1+10
	if tank_go_down(x_tank2,y_tank2):
		x_tank2=x_tank2+1
		y_tank2=y_tank2+10
	showmap(angle1,speed1,angle2,speed2,is_explosion1,is_explosion2,small_proj1,small_proj2)
	if life1<=0 or life2<=0:
		running=False

	pygame.display.update()
# afisare castigator
pygame.time.delay(500)
end_screen=pygame.display.set_mode((width,length))
if life1<=0 or life2<=0:
	end_window=True
while end_window==True:
	end_screen.fill((0,0,0))
	pygame.mixer.Sound.play(win_sound)
	pygame.mixer.music.stop()
	
	if life1<=0:
		end_screen.blit(text8,textRect8)
	if life2<=0:
		end_screen.blit(text9,textRect9)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			end_window=False
	pygame.display.update()

