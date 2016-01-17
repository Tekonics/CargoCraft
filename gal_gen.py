









def sys_gen(x):
    fr = open('gal.txt')

    lines=fr.readlines()
    x = lines[x]
    print x
    fr.close()

sys_gen(3)

print 
