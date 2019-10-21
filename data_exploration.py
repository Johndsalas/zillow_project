from scipy import stats

def get_t_test(var_1,var_2):

    print("T-test Results:")
    print(stats.ttest_ind(var_1, var_2))


def get_pearsons_r(var_1,var_2):

    print("Pearson's r Results:")
    print(stats.pearsonr(var_1,var_2))


    