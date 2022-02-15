import sys

#Input: three integers. First argument > 0, second argument >= 0, third argument = 1 or 0.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
#Output: string where the text of the song is formed by verses separated by spaces.
t1 = (' la' + '-la' * (x - 1)) * y 
t2 = '.'
if z == 1:
    t2 = '!'
print("Everybody sing a song:" + t1 + t2)