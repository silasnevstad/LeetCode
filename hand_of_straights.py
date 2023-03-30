class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for card in hand:
            if card not in count:
                count[card] = 1
            else:
                count[card] += 1
                
        for card in sorted(count):
            if count[card] > 0:
                for i in range(1, groupSize):
                    if card + i not in count or count[card + i] < count[card]:
                        return False
                    count[card + i] -= count[card]
        
        return True