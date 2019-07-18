#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8


# In[ ]:


import sys
from datetime import datetime
from translate import Translator
import locale

locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

## dia del programador 


# In[ ]:


# Validar si el año es correcto

def validate_year(year):
	try:
   		value_year = int(year)
   		validate_year = value_year > 0 and len(year) == 4
   		if validate_year == False:
   			print("Year is not valid")
   		return validate_year
	except ValueError:
   		print("Year is not validate")
   		return False


# In[ ]:


# Validar si el día corresponde al rango 
def validate_day(day):
	try:
		value_day = int(day)
		validate_range=range(1,366)
		day_correct = value_day in validate_range
		if day_correct is False:
			print("Day is not valid")			
		return day_correct
	except ValueError:
		print("Day is not valid")
		return False


# In[ ]:


# Traducir al ruso el día y el mes del año
def translate_word(word,translate_lang):
	translator= Translator(from_lang='spanish', to_lang=translate_lang)
	translation = translator.translate(word)
	
	return translation


# In[ ]:


# Validar el día del programdor de acuerdo al año y el día
def get_year_day(year,day):
	val_year = validate_year(year)
	val_day = validate_day(day)
	if val_year and val_day:
		int_year = int(year)
		date = str(year) + " " + str(day)
		get_date = datetime.strptime(date, '%Y %j')
		get_month = get_date.strftime('%B')
		get_day = get_date.strftime('%A')
		get_day_w = get_date.strftime('%d')
		range_years = range(2003,2009)
		now = datetime.now()
		if int_year < 2003:
			print('Oh, Esta celebración no existia aún')		
		elif int_year in range_years:
			get_month_translate = translate_word(get_month,'russian')
			get_day_translate = translate_word(get_day,'russian')
			print("Den' programmista {} goda sostoyalsyao {}  {}  iz {}".format(year,get_day_translate,get_day_w,get_month_translate))
		elif get_date.strftime('%y%m%d')< now.strftime('%y%m%d') :
			print("El día del programador del a\u00f1o {} se celebró el {}  {} de {}".format(year,get_day,get_day_w,get_month))
		elif get_date.strftime('%y%m%d')> now.strftime('%y%m%d') :
			print("El día del programador del a\u00f1o {} se celebrará el {}  {} de {}".format(year,get_day,get_day_w,get_month))
		elif get_date.strftime('%y%m%d') == now.strftime('%y%m%d'):
			print("EL día del programador se celebra hoy! Felicidades!")


# In[ ]:


def main(args):
	if len(sys.argv)-1 == 1:
		year = args[1]
		day = 256
		get_year_day(year,day)
	elif len(sys.argv)-1 == 2:
		year = args[1]
		day = args[2]
		get_year_day(year,day)
	else:
		print("Error, Please  put a year (or a day if you want)")


# In[ ]:


if __name__ == '__main__':
    main(sys.argv)

