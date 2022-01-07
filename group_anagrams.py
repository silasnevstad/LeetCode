class Solution(object):
    def groupAnagrams(self, strs):
        lookup = {}
        output = []

        for word in strs:
            sorted_word = list(word)
            sorted_word.sort()

            curr_word = str("".join(sorted_word))

            if curr_word in lookup:
                lookup[curr_word] = lookup[curr_word] + [word]
            else:
                lookup[curr_word] = [str(word)]

        for key in lookup:
            output.append(lookup[key])

        return output
