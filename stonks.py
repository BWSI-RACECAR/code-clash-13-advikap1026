class Solution:
    def stonks(self, prices):
            #type prices: list of int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            lowest = prices[0]
            lowIndex = 0 
            for i in range(len(prices)): 
                 if prices[i] < lowest: 
                      lowest = prices[i]
                      lowIndex = i 
            highest = prices[lowIndex]
            highInd = lowIndex
            for i in range(lowIndex, len(prices)):
                 if prices[i] > highest:
                      if prices[i]> lowest: 
                        highest = prices[i]
                        highInd = i 
            profit = highest - lowest
            return profit 

            highestProfit = 0 
            for i in range(len(prices)):
                 lowInd = i 
                 lower = prices[i]
                 for j in range(i, len(prices)):
                      highInd = j 
                      higher = prices[j]
                      firstProfit = higher - lower 
                
                 
            
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()