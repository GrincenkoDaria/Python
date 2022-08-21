name="Ivan"
midlName="Ivanovich"
balance= 3444
text="Dorogoj {0} {1}, balans vashego licevogo scheta sostavlaet {2} rub.".format(name,midlName,balance)
print(text)
text="Dorogoj {mn} {n}, balans vashego licevogo scheta sostavlaet {b} rub.".format(n=name,mn=midlName,b=balance)
print(text)