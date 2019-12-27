from sqlalchemy import create_engine


connect_info_1 = 'mssql+pymssql://sa:123456@10.10.110.100:1433/mta'

engine_1 = create_engine(connect_info_1)


def get_data(user_name, start_time, end_time):
    pass
