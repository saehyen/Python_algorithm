String = input()
Search = input()
answer = 0
i = 0
while i <= len(String)-len(Search) :
    if String[i:i+len(Search)] == Search :
        i += len(Search)
        answer += 1
    else : 
        i += 1
print(answer)