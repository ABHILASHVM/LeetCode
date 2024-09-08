# class Solution:
#     def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
#         left=0
#         total=0
#         full=numBottles
#         while full != 0 and left < numExchange:
#             if (full//numExchange) !=0:
#                 total=total+full
#                 full=(full//numExchange)
#                 left=left+(full%numExchange)
                
#             else:
#                 left=left+full
#                 total=total+full
#                 full=0
#             if left>=numExchange:
#                 full=full+(left//numExchange)
#                 left=left%numExchange
#         return total-full
#             # numBottles=full+left
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            total_drunk += new_bottles
            empty_bottles = empty_bottles % numExchange + new_bottles
        
        return total_drunk