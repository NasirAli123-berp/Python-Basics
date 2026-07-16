#Topic: Break, Continue & Pass 
#Description: Learning how to control the flow of loops in Python 
#Author: Nasir Ali 

#What are break, continue and pass?
#They are control statements used to change the normal execution of loops.

#یہ statement loopکے چلنے کے طریقے کو  کنٹرول کرتی ہے۔کبھی لوپ کو روک دیتی ہے ۔کبھی ایک iteration کو Skip کرتی ہے ۔اور کبھی کچھ بھی نہیں کرتیں ۔

#break 
#جب شرط پوری ہو جائے تو لپ کو فوراً ختم کر دیتا ہے 
for i in range(1,11):
    if i == 6:
        break
    print(i)

#output 
# 1
# 2
# 3

# continue 
#صرف موجودا iteration کو skip کرتا ہے لوپ کو ختم نہیں کرتا۔
for i in range(1,8):
	if i == 4:
		continue 
	print(i)
	
# pass
#کچھ بھی نہیں کرتا۔
#یہ صرف placeholder ہے۔

for i in range(1,5):
	if i == 2:
		pass
	print(i)
	
# Mini Practice 
for i in range(1,11):
        if i == 6:
            break
        print(i)
     
for i in range(1,8):
	if i % 2 == 0:
		continue 
	print(i)
	
for i in range(6):
	if i == 3:
		pass
	print(i)
	
#What I learned
# break
# continue
# pass

# Interview Questions 
# 1. What is break?
# 2. What is continue?
# 3. What is pass?
# 4. What is the difference between break and continue?
# 5. When do we use pass? 

#Note:
# break stops the entire loop.
# continue skips the current iteration.
# pass does nothing and acts as a placeholder.
