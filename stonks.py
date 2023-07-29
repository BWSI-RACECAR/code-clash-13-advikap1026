class Solution:
    def stonks(self, prices):
            #type prices: list of int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            print(prices)
            # lowest = prices[0]
            # lowIndex = 0 
            # for i in range(len(prices)): 
            #      if prices[i] < lowest: 
            #           lowest = prices[i]
            #           lowIndex = i 
            # highest = prices[lowIndex]
            # highInd = lowIndex
            # for i in range(lowIndex, len(prices)):
            #      if prices[i] > highest:
            #           if prices[i]> lowest: 
            #             highest = prices[i]
            #             highInd = i 
            # profit = highest - lowest
            # return profit 

            # highestProfit = 0 
            # firstProfit = 0 
            # secondProfit = 0 
            # for i in range(len(prices)):
            #      lowInd = i 
            #      lower = prices[i]
            #      for j in range(i, len(prices)):
            #         highInd = j 
            #         higher = prices[j]
            #         if higher > lower: 
            #             firstProfit = higher - lower 
            #         else: 
            #             continue
                    
            #         for k in range(j, len(prices)):
            #             secondLowInd = k 
            #             secondLow = prices[k]
            #             for l in range(k, len(prices)):
            #                 secondHigh = prices[l]
            #                 if secondHigh > secondLow: 
            #                     secondProfit = secondHigh - secondLow 
            #      profit = secondProfit + firstProfit
            #      if profit >highestProfit:
            #         highestProfit = profit 
            # return highestProfit
                    
            # length = len(prices)
            # if length == 0:
            #     return 0
            # max_profit, low = 0, prices[0]
            # for i in range(1, length):
            #     if low > prices[i]:
            #         low = prices[i]
            #     else:
            #         temp = prices[i] - low
            #         if temp > max_profit:
            #             max_profit = temp
            # return max_profit
                 
            buy1 = buy2 = float('-inf')
            sell1 = sell2 = 0

            for price in prices:
                buy1 = max(buy1, -price)
                sell1 = max(sell1, buy1 + price)
                buy2 = max(buy2, sell1 - price)
                sell2 = max(sell2, buy2 + price)

            return sell2
            
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