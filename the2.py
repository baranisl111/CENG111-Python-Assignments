def check_month(month_calendar):
	a = month_calendar
	Uymayan_Rulelar = []

	#RULE_1
	ms = a.count("m")

	if 0 <= ms <= 1:
		pass

	elif 2 <= ms <= 5:
		index_m = [i for i,m in enumerate(a) if m =="m"]
		farklar = [index_m[0]-b for b in index_m[1:]]
		uyuyor_mu = all(fark%5==0 for fark in farklar)
		
		if uyuyor_mu==True:
			pass
		else:
			Uymayan_Rulelar.append(1)
		  	    
	else:
		Uymayan_Rulelar.append(1)
		
	#RULE_2
	fs = a.count("f")

	if 0 <= fs <= 1:
		pass 

	elif fs == 2:
		index_f = [i for i,f in enumerate(a) if f=="f"]
		if index_f[1]-index_f[0]==1:
			if index_f[0] in [4,9,14,19]:
				pass 
			else:
				Uymayan_Rulelar.append(2) 
		else:
			pass 
	else:	
		Uymayan_Rulelar.append(2) 
		
	#RULE 4
	index_g = [i for i,g in enumerate(a) if g=="g"] 
	k = [indexg for indexg in index_g if indexg in [2,7,12,17]]
		
	if len(k) > 1:
		Uymayan_Rulelar.append(4)
	else:
		pass
			
	#RULE 5
	index_a1 = [i for i,a1 in enumerate(a) if a1 == "a1"]
	uygun_a1 = [i for i in index_a1 if i in [1,6,11,16,21,4,9,14,19]]
	if index_a1 == uygun_a1:
		pass
	else:
		Uymayan_Rulelar.append(5)

	#RULE 6
	index_a2 = [i for i,a2 in enumerate(a) if a2 == "a2"]
	a2_a1_farkları = [a2-a1 for a2 in index_a2 for a1 in index_a1]

	if 1 in a2_a1_farkları:
		a1_a2_ikilileri = [(a1,a2) for a1 in index_a1 for a2 in index_a2 if a2-a1==1]
		a1s = [a1x for (a1x,b) in a1_a2_ikilileri]
		cuma_mı = [a for a in a1s if a not in [4,9,14,19]]
		
		if len(cuma_mı)>0:
			Uymayan_Rulelar.append(6)
		else:
			pass
			
	else:
		pass

	#RULE 7
	index_n = [i for i,n in enumerate(a) if n == "n"]
	uygun_n = [i for i in index_n if i in [0,1,2,5,6,7,10,11,12,15,16,17,20,21]]
	if index_n == uygun_n:
		pass
	else:
		Uymayan_Rulelar.append(7)

	#HESAPLAMA
	mother_cost = a.count("m")*10

	father_cost = a.count("f")*20

	#Babysitter Cost
	babysitter_day = a.count("b")
	if len(a)==20 or len(a)==21 or len(a)==22:
		if a[4] == a[5] == "b":
			babysitter_day += 2
			
		if a[9] == a[10] == "b":
			babysitter_day += 2
			
		if a[14] == a[15] == "b":
			babysitter_day += 2
			
		if len(a) > 20:
			if a[19] == a[20] == "b":
				babysitter_day += 2
			
		if (a[0]==a[2]=="b" or a[0]==a[3]=="b") and a[1]!="b":
			 babysitter_day += 1

		if (a[1]==a[3]=="b" or a[1]==a[4]=="b" or a[0]==a[3]=="b") and a[2]!="b":
			babysitter_day += 1
			
		if (a[1]==a[4]=="b" or a[2]==a[4]=="b") and a[3]!="b":
			 babysitter_day += 1
				
		if (a[5]==a[7]=="b" or a[5]==a[8]=="b") and a[6]!="b":
			 babysitter_day += 1

		if (a[6]==a[8]=="b" or a[6]==a[9]=="b" or a[5]==a[8]=="b") and a[7]!="b":
			babysitter_day += 1
			
		if (a[6]==a[9]=="b" or a[7]==a[9]=="b") and a[8]!="b":
			 babysitter_day += 1
			
		if (a[10]==a[12]=="b" or a[10]==a[13]=="b") and a[11]!="b":
			 babysitter_day += 1

		if (a[11]==a[13]=="b" or a[11]==a[14]=="b" or a[10]==a[13]=="b") and a[12]!="b":
			babysitter_day += 1
			
		if (a[11]==a[14]=="b" or a[12]==a[14]=="b") and a[13]!="b":
			 babysitter_day += 1
			
		if (a[15]==a[17]=="b" or a[15]==a[18]=="b") and a[16]!="b":
			 babysitter_day += 1

		if (a[16]==a[18]=="b" or a[16]==a[19]=="b" or a[15]==a[18]=="b") and a[17]!="b":
			babysitter_day += 1
			
		if (a[16]==a[19]=="b" or a[17]==a[19]=="b") and a[18]!="b":
			 babysitter_day += 1

	babysitter_cost = babysitter_day*30

	grandma_cost = a.count("g")*50

	aunt1_cost = a.count("a1")*32

	aunt2_cost = a.count("a2")*27

	nc = a.count("n")

	if nc > 1:
		nckk = [k for k in range(1,nc)]
		neighbour_cost = sum([5**a for a in nckk])
		
	else:
		neighbour_cost = 0
		


	if Uymayan_Rulelar == []:
		return(mother_cost + father_cost + babysitter_cost + grandma_cost + aunt1_cost + aunt2_cost + neighbour_cost)
		
		
	else:
		return(Uymayan_Rulelar)
		



		








