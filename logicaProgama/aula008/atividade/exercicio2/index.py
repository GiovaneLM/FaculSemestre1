   ##
  ####
 ######
########
 ######
  ####
   ##


coluna = 4

top = [((" " * (coluna - linha) +"##" * linha)) for linha in range (1,coluna+1)]
print("{}\n{}".format("\n".join(top),"\n".join(top[-2::-1])))