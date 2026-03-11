class Solution:
    def compress(self, chars: List[str]) -> int:

        count = 1
        result = []

        for i in range(1, len(chars)):

            if chars[i] == chars[i-1]:
                count += 1

            else:
                result.append(chars[i-1])

                if count > 1:
                    for digit in str(count):
                        result.append(digit)

                count = 1

        result.append(chars[-1])

        if count > 1:
            for digit in str(count):
                result.append(digit)

        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)

        