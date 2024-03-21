class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        a = -1
        z = -1
        i = 0
        x = 0
        status = True
        if len(flowerbed) == 0:
            return False
        elif len(flowerbed) == 1:
            if flowerbed[0] == 0 :
                return 1>=n 
            else:
                return 0>=n
        else:
            while status:
                if a < 0 and flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    a = i
                    z = i+1
                    x += 1

                if ((a+2)==z) or ((z+2)==a):
                    if z==len(flowerbed)-1:
                        x+=1
                    
                    elif flowerbed[z+1] != 1 and flowerbed[z-1] != 1 and (z-a) != abs(1):
                        x+=1
                        a = z

                if flowerbed[i] == 1:
                    a = i

                if flowerbed[i] == 0:
                    z = i
                    if (z-a) != abs(1) and z == len(flowerbed)-1:
                        x+=1
                        a=z

                if len(flowerbed)-1 == i:
                    status = False

                i+=1

            return x>=n