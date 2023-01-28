class Diff():

    def __init__(self, ratio=1):
        self.ratio = ratio

    def compute(self, value_list):
        diff_list = []
        i = 0
        j = i + 1

        while j < len(value_list):

            diff = value_list[j] - value_list[i]

            diff_list.append(diff)

            i = i + 1
            j = j + 1

        if self.ratio != 1:
            for idx, diff in enumerate(diff_list):
                diff_list[idx] = diff_list[idx] / self.ratio

        return diff_list


diff = Diff(2)
result = diff.compute([2, 4, 8, 16])
print(result)
