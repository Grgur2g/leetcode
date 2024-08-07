class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        extra = { 9: 'Billion', 6: 'Million', 3: 'Thousand', 2: 'Hundred' }

        translate = { 0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
            8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tens =  {
            2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}

        def check(curr,rj):
            curr = int(curr)
            if curr > 99:
                x = int(str(curr)[0])
                rj.append(translate[x])
                rj.append(extra[2])
                x *= 100
                curr = curr - x
            if curr < 20:
                if curr == 0: return
                rj.append(translate[curr])
            else:
                rj.append(tens[curr//10])
                if curr%10 == 0: return
                rj.append(translate[curr%10])

        kopija = str(num)
        rj = []
        curr = ""
        for n in str(num):
            curr += n
            kopija=kopija[1:]
            if len(kopija) in [9,6,3,2]:
                check(curr,rj)
                if int(curr) > 0:
                    rj.append(extra[len(kopija)])
                curr = ""
        check(curr,rj)
        return ' '.join(rj)


# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"

# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
