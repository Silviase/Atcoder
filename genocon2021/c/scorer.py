import matplotlib.pyplot as plt

TESTCASE_PATH = "./read/"
TESTCASE_NUM = 100


class Scorer:
    def __init__(self, alignment_func):
        self.score_small = []
        self.score_large = []
        self.fn = alignment_func

    def test(self, mode="s"):
        for i in range(TESTCASE_NUM):
            test_path = TESTCASE_PATH + "test_ssim_" + str(i).zfill(2) + ".txt"
            with open(test_path, "r") as f:
                file = f.readlines()
                N = int(file[0])
                genoms = file[1:]
                result = self.fn(genoms, N)
                score = calc_score(result)
                self.score_small.append(score)

        if mode == "l":
            for i in range(TESTCASE_NUM):
                test_path = TESTCASE_PATH + "test_lsim_" + str(i).zfill(
                    2) + ".txt"
                with open(test_path, "r") as f:
                    file = f.readlines()
                    N = int(file[0])
                    genoms = file[1:]
                    result = self.fn(genoms, N)
                    score = calc_score(result)
                    self.score_small.append(score)

    def visualize_score(self, mode="s"):
        self.test(mode=mode)
        if mode == "s":
            plt.plot(range(TESTCASE_NUM), self.score_small)
            plt.show()
        elif mode == "l":
            plt.plot(range(TESTCASE_NUM), self.score_large)
            plt.show()

    def calc_score(alignment_table):
        score = 0

        return score