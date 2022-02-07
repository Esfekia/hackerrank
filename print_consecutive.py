n = int(raw_input())
if n > 0 and n < 151:
     start = 1
      str_result = ""
       while start <= n:
            str_result = str_result+str(start)
            start += 1
        print(str_result)
