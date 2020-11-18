class Solution:

    dicti = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:

        result = self.dicti[s[-1]]
        last_num = s[-1]

        # Для проверки валидности строки
        decr_seq = 0

        for snum in s[-2::-1]:
            if self.dicti[snum] < self.dicti[last_num]:
                result -= self.dicti[snum]

                # Учёт длины убывающей последовательности
                decr_seq += 1
                if decr_seq > 1:
                    raise Exception(f"{s} is invalid sequence")
            else:
                # Учёт длины нестрого убывающей последовательности
                if decr_seq >= 1 and self.dicti[snum] == self.dicti[last_num]:
                    raise Exception(f"{s} is invalid sequence")
                decr_seq = 0

                result += self.dicti[snum]

            last_num = snum
        return result


if __name__ == "__main__":
    print("I =", Solution().romanToInt("I"))  # 1
    print("III =", Solution().romanToInt("III"))  # 3
    print("IX =", Solution().romanToInt("IX"))  # 9
    print("LVIII =", Solution().romanToInt("LVIII"))  # 58
    print("MCMXCIV =", Solution().romanToInt("MCMXCIV"))  # 1994
    try:
        print("MCMXCIV =", Solution().romanToInt("IIV"))  # Error
    except Exception as ex:
        print(repr(ex))
