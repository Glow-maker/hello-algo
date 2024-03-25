import pandas as pd

"""
找出没有任何与名为 “RED” 的公司相关的订单的所有销售人员的姓名。

以 任意顺序 返回结果表。
"""


def no_sales_person_for_red_company():
    data = [[1, 'John', 100000, 6, '4/1/2006'], [2, 'Amy', 12000, 5, '5/1/2010'], [3, 'Mark', 65000, 12, '12/25/2008'],
            [4, 'Pam', 25000, 25, '1/1/2005'], [5, 'Alex', 5000, 10, '2/3/2007']]
    sales_person = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype(
        {'sales_id': 'Int64', 'name': 'object', 'salary': 'Int64', 'commission_rate': 'Int64',
         'hire_date': 'datetime64[ns]'})
    data = [[1, 'RED', 'Boston'], [2, 'ORANGE', 'New York'], [3, 'YELLOW', 'Boston'], [4, 'GREEN', 'Austin']]
    company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype(
        {'com_id': 'Int64', 'name': 'object', 'city': 'object'})
    data = [[1, '1/1/2014', 3, 4, 10000], [2, '2/1/2014', 4, 5, 5000], [3, '3/1/2014', 1, 1, 50000],
            [4, '4/1/2014', 1, 4, 25000]]
    orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype(
        {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'com_id': 'Int64', 'sales_id': 'Int64',
         'amount': 'Int64'})

    # df = sales_person.merge(orders, on='sales_id', how='left')
    # df_com = df.merge(company, on='com_id', how='left')
    # df_out = df_com[df_com['name_y'] == 'RED']['name_x'].drop_duplicates()
    # return df_out
    # return df_com[df_com['name'] != 'RED']['name'].drop_duplicates()
    return sales_person[~sales_person['sales_id'].isin(
        orders[orders['com_id'].isin(company[company['name'] == 'RED']['com_id'])]['sales_id'])]['name']


def sale_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = sales_person.merge(orders, on='sales_id', how='left')
    df2 = (df1.merge(company, on='com_id', how='left')
           .groupby('name_x').filter(lambda x: 'RED' not in x['name_y'].values))
    df3 = df2[['name_x']].rename(columns={'name_x': 'name'}).drop_duplicates()

    # df1 = (sales_person.merge(orders, on='sales_id', how='left')
    #        .merge(company, on='com_id', how='left')
    #        .groupby('name_X').filter(lambda x: True if 'RED' not in x['name_y'].values else False))
    return df3


def accepted_candidates() -> pd.DataFrame:

    data = [[11, 'Atticus', 1, 101], [9, 'Ruben', 6, 104], [6, 'Aliza', 10, 109], [8, 'Alfredo', 0, 107]]
    candidates = pd.DataFrame(data, columns=['candidate_id', 'name', 'years_of_exp', 'interview_id']).astype(
        {'candidate_id': 'Int64', 'name': 'object', 'years_of_exp': 'Int64', 'interview_id': 'Int64'})
    data = [[109, 3, 4], [101, 2, 8], [109, 4, 1], [107, 1, 3], [104, 3, 6], [109, 1, 4], [104, 4, 7], [104, 1, 2],
            [109, 2, 1], [104, 2, 7], [107, 2, 3], [101, 1, 8]]
    rounds = pd.DataFrame(data, columns=['interview_id', 'round_id', 'score']).astype(
        {'interview_id': 'Int64', 'round_id': 'Int64', 'score': 'Int64'})

    df = rounds.groupby('interview_id').apply(lambda x: x.score.sum()).rename('cnt').reset_index()
    df2 = df.merge(candidates, on='interview_id', how='left')
    df3 = df2.groupby('candidate_id').filter(lambda x: (x['cnt'] > 15) & (x['years_of_exp'] > 2))

    print(df)
    return df3[['candidate_id']]


if __name__ == '__main__':

    accepted_candidates()
