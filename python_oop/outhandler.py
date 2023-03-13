
col:list=["Idno","Lastname","Firstname","Course","Level"]
lenc = max(len(i) for i in col)
def outputHandler(title,a,b,c,d,e):
    print(f"Student {title}!\n------------------------")
    print("{:<{}}".format("Idno", lenc+3)+ " : " + "{:<{}}".format(a,lenc+3))
    print("{:<{}}".format("Lastname", lenc+3)+ " : " + "{:<{}}".format(b,lenc+3))
    print("{:<{}}".format("Firstname", lenc+3)+ " : " + "{:<{}}".format(c,lenc+3))
    print("{:<{}}".format("Course", lenc+3)+ " : " + "{:<{}}".format(d,lenc+3))
    print("{:<{}}".format("Level", lenc+3)+ " : " + "{:<{}}".format(e,lenc+3))
                    