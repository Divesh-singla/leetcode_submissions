class Solution:
    def compress(self, chars: List[str]) -> int:
        # chars = ["a","a","b","b","c","c","b","a","c","c","c"]
        # chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        # chars=["b","b"]
        # chars=["a"]
        index = 1
        count = 1
        firstApp = None
        status = True
        element = chars[0]

        if len(chars)>1:
            while status:
            #     try:
                if element == chars[index]:
                    count+=1
                    
                    if count==2:
                        firstApp = index
                    else:
                        pass

                else:
                    if count>=2:

                        element = chars[index]
                        inter = str(count)
                        for x in range(len(inter)):
                            chars[firstApp+x] = inter[x]
                        del(chars[firstApp+len(inter):index])
                        index=firstApp+len(inter)
                        count=1
                    else:
                        element = chars[index]
                        count=1
                # print(chars,firstApp,element)
                index+=1


                if len(chars)-1<index:
                    # print("yesss",index,firstApp)
                    if count>=2:
                        inter = str(count)
                        for x in range(len(inter)):
                            chars[firstApp+x] = inter[x]
                        del(chars[firstApp+len(inter):index])
        #                 del(chars[firstApp+1:])
                    else:
                        pass
                    status = False

        else:
            pass
                    
            
        return(len(chars))

        