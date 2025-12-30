class user: 
    def __init__(self,oily,dry,acne,flaky):
        self.oily = oily 
        self.dry = dry 
        self.acne = acne 
        self.flaky = flaky

class analyse_skin_type: 
    def skin_type(self,user): 
        if not user.oily and not user.acne and not user.dry and not user.flaky: 
            return "Normal"
        elif user.oily and user.dry: 
            return "Combination"
        elif user.oily or user.acne:
            return "oily"
        elif user.dry or user.flaky:
            return "Dry"
        else: 
            return "Combination"
    

def questions(q):
    answer = input(q + " yes/no: ")
    return answer == "yes"

oily = questions("Does your skin feel oily frequently?")
acne = questions("Do you notice frequent acne formation?")
dry = questions("Does you skin get dry easily?")
flaky = questions("Does youy skin feel flaky?")

user1 = user(oily,dry,acne,flaky)

analyse = analyse_skin_type()
result = analyse.skin_type(user1)

print("Determined skin type is:" , result)


        