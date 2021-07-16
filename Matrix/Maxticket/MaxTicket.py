def maxTickets(tickets):
 tickets.sort()
 n = len(tickets)
 i = 0
 ans = 0
 while(i < n):
    j = i + 1
    while(j < n and tickets[j] - tickets[j - 1] <= 1):
        j = j + 1
        ans = max(ans, j - i)
        i = j
 return ans