class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total_gas_remaining = 0
        current_gas_remaining = 0
        starting_station = 0
        
        for i in range(n):
            total_gas_remaining += gas[i] - cost[i]
            current_gas_remaining += gas[i] - cost[i]
            
            if current_gas_remaining < 0:
                starting_station = i + 1
                current_gas_remaining = 0
                
        return starting_station if total_gas_remaining >= 0 else -1