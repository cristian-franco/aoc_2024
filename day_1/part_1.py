import pandas as pd
from tqdm import tqdm


def determine_diff(
    num_1: int,
    num_2: int
) -> int:
    '''
    Given two integers, will find the absolute distance
    between the two.
    '''

    diff = abs(num_1 - num_2)

    return diff


def read_input():
    df = pd.read_csv(
        'input/day_1_input.txt',
        sep="  ",
        header=None,
        engine='python'
    )

    df.columns = ["list_1_id", "list_2_id"]

    print(type(df.iloc[0]))
    print(df.iloc[0])

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
    diff_sum = 0
    for item in tqdm(list_1):
        min_1 = list_1[counter]
        min_2 = list_2[counter]

        diff = determine_diff(min_1, min_2)
        # print(
        #     f"min_1 = {min_1}\n"
        #     f"min_2 = {min_2}\n"
        #     f"diff = {diff}\n"
        # )

        diff_sum = (
            diff_sum
            + diff
        )

        counter += 1

    print(
        str(diff_sum)
    )

    return

if __name__ == '__main__':
    main()
