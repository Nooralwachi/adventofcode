def passport(file):
	line_number =0
	line=[]
	valid=0
	needed_fields=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
	eye=['amb', 'blu' ,'brn', 'gry', 'grn', 'hzl' ,'oth']
	f = open(file, "r")	
	line.append(f.read())
	values=line[0].split("\n\n")
	for value in values:
		line_number +=1
		available =needed_fields[:]
		pp =(" ").join(value.split("\n"))
		fields =pp.split(" ")
		for x in fields:
			if str(x):
				fld= x[0:3]
				year = x[4:8]
				hgt = x.split(":")[1][:-2]
				typ = x[-2:]
				color = x[-7:]
				ecl = x[-3:]
				pid = x.split(":")[1]			
				if fld in available:
					if fld == 'byr' and int(year)>=1920 and int(year) <=2002:
						available.remove(fld)
					elif fld == 'iyr' and int(year)>=2010 and int(year) <=2020:
						available.remove(fld)
					elif fld == 'eyr' and int(year)>=2020 and int(year) <=2030:
						available.remove(fld)
					elif fld == 'hgt' and typ =='cm' and int(hgt)>=150 and int(hgt) <=193:
						available.remove(fld)
					elif fld == 'hgt' and typ =='in'and int(hgt)>=59 and int(hgt) <=76:
						available.remove(fld)
					elif fld == 'hcl' and len(color)==7 and x[-7] == '#':						
						available.remove(fld)
					elif fld == 'ecl' and ecl in eye:
						available.remove(fld)
					elif fld == 'pid' and len(pid)==9:
						available.remove(fld)
		if len(available)>0 :
			if available[0]=='cid':
				valid+=1
		else:
			valid+=1
	print(valid)


passport("passport.txt")