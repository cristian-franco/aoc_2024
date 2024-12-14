import pandas as pd
from tqdm import tqdm


def find_num_instances(
    num_1: int,
    list_2
) -> int:
    '''
    Given an integer, find how many times
    it shows up in the given list.
    '''

    num_instances = list_2.count(num_1)

    return num_instances


def read_input():
    df = pd.read_csv(
        'input/day_1_input.txt',
        sep="  ",
        header=None,
        engine='python'
    )

    df.columns = ["list_1_id", "list_2_id"]

    # print(df)

    list_1 = list(df['list_1_id'])
    list_2 = list(df['list_2_id'])

    list_1.sort(reverse=True)
    list_2.sort(reverse=True)

    return list_1, list_2

def main():

    list_1, list_2 = read_input()

    print(
        f"List 1 length: {len(list_1)}\n"
        f"List 2 length: {len(list_2)}"
    )

    counter = 0
    score_sum = 0
    for item in tqdm(list_1):
        min_1 = list_1[counter]

        num_instances = find_num_instances(min_1, list_2)
        # print(
        #     f"min_1 = {min_1}\n"
        #     f"min_2 = {min_2}\n"
        #     f"diff = {diff}\n"
        # )

        score_sum = (
            score_sum
            + (num_instances * min_1)
        )

        counter += 1

    print(
        str(score_sum)
    )

    return

if __name__ == '__main__':
    main()
