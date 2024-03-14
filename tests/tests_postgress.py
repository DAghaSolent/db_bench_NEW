import datetime as dt
from streamlit.testing.v1 import AppTest

#NOTE Currently needs to be run using - 'pytest .\tests\tests_clickhouses.py -v' - May need to be in the VM to run it correctly

def test_1_downsample_clickhouse_enable():
    """A test to check whether the downsample toggle can be clicked to enable it"""
    at = AppTest.from_file("db_bench.py").run()
    assert at.toggle(key="downsample_toggle_clickhouse").run()

# def test_2_increment_downsample_value_clickhouse(): #NOTE For some reason this doesn't recognise the key - Will look into it
#     """A test to increment the downsample number input"""
#     at = AppTest.from_file("db_bench.py").run()
#     at.number_input(key="downsample_value_clickhouse").increment().run()
#     assert at.number_input(key="downsample_value_clickhouse").value == 1

# def test_5_check_radio_values_clickhouse(): #NOTE For some reason this doesn't recognise the key - Will look into it
#     """A test to check the default values of the radio buttons"""
#     at = AppTest.from_file("db_bench.py").run()
#     assert at.radio(key="clickhouse_downsample_time").options["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"]
    
# def test_8_change_radio_values_clickhouse(): #NOTE For some reason this doesn't recognise the key - Will look into it
#     """A test to check the default values of the radio buttons"""
#     at = AppTest.from_file("db_bench.py").run()
#     at.radio(key="clickhouse_downsample_time").set_value("Hours").run()
#     assert at.radio(key="clickhouse_downsample_time").value == "Hours"

def test_11_set_start_date_value_clickhouse():
        """A test to set the clickhouse start date"""
        at = AppTest.from_file("db_bench.py").run()
        at.date_input(key="start_date_clickhouse").set_value(dt.date(2024, 1, 1)).run()
        assert at.date_input(key="start_date_clickhouse").value == dt.date(2024, 1, 1)

def test_14_set_end_date_value_clickhouse():
        """A test to set the clickhouse end date"""
        at = AppTest.from_file("db_bench.py").run()
        at.date_input(key="end_date_clickhouse").set_value(dt.date(2019, 6, 6)).run()
        assert at.date_input(key="end_date_clickhouse").value == dt.date(2019, 6, 6)

# def test_17_set_start_time_value_clickhouse(): #NOTE For some reason this doesn't recognise the key - Will look into it
#        """A test to set the clickhouse start time"""
#         at = AppTest.from_file("db_bench.py").run()
#         at.time_input(key="start_time_clickhouse").set_value(dt.time(13, 50))
#         assert at.date_input(key="start_time_clickhouse").value == (dt.time(13, 50),) #Dates in a weird format for some reason

# def test_20_set_end_time_value_clickhouse(): #NOTE For some reason this doesn't recognise the key - Will look into it
#        """A test to set the clickhouse end time"""
#         at = AppTest.from_file("db_bench.py").run()
#         at.time_input(key="end_time_clickhouse").set_value(dt.time(7, 30))
#         assert at.date_input(key="end_time_clickhouse").value == (dt.time(7, 30),) #Dates in a weird format for some reason

def test__submit_clickhouse(): #NOTE For some reason this doesn't recognise the key - Will look into it
        """A test to click the submit button and start collecting clickhouse data"""
        at = AppTest.from_file("db_bench.py").run()
        assert at.button(key="submit_clickhouse").click().run()