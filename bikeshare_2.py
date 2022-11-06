"""
Welcome to my code..Muhammed  2022.....
"""
import time
import pandas as pd


"""
The Dictionary Bellow has the city as a key and the value
is the corresponding csv file which is stored on the same directory 
"""
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
"""
Month Data array
"""
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
"""
Day Data array
"""
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Let\'s explore some US bikeshare data')
    # First we initilise the city varible name
    city_name = ''

    while city_name.lower() not in CITY_DATA:
        # getting user input

        city_name = input("\nPlease choose a city (chicago, new york city, washington)\n")

        if city_name.lower() in CITY_DATA:
            # city name by user matches the actual one from avaliable options
            city = CITY_DATA[city_name.lower()]

        else:
            # NO matches
            print("Please enter correct name")
    # Next... we obtain the month data
    # First we initilise the Month varible name
    month_name = ''

    while month_name.lower() not in MONTH_DATA:
        month_name = input(
            "\n Please choose a Month (Input either 'all' to apply no month filter or january,february..june)\n")
        if month_name.lower() in MONTH_DATA:
            # user chose correct option
            month = month_name.lower()
        else:
            # User typed error
            print(" Please type in correct option with correct spelling")
    # Next... we obtain the day data
    # First we initilise the day varible name
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input(
            " Choose a day please...(Input either 'all' to apply no day filter or monday, tuesday,..sunday)\n")
        if day_name.lower() in DAY_DATA:
            # User chose correct option
            day = day_name.lower()
        else:
            # User wrote wrong name
            print("Please check name or spelling..")
    print('-' * 40)

    return city, month,day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print(" Setting up the Data for you.....")
    df = pd.read_csv(city)
    # When a csv file is imported and a Data Frame is made,
    # the Date time objects in the file are read as a string object rather a Date Time object and
    # Hence it’s very tough to perform operations like Time difference on a string rather a Date Time object.
    # Pandas to_datetime() method helps to convert string Date time into Python Date time object.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    # Now we need to filter by month

    if month != 'all':
        month = MONTH_DATA.index(month)
    # filtering by the specofied month
        df = df.loc[df['month'] == month]
    # filtering by the specofied day as said by user
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    # time.time() method of Time module is used to get the time in seconds since epoch.

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('The most frequent month on record is: ' + MONTH_DATA[common_month].title())

    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most freq day of week is: ' + str(common_day_of_week))

    common_start_hour = df['hour'].mode()[0]
    print("The most common hour is : " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print("Most used Start Station: " + common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print("Most used End Station: " + common_end_station)

    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most Freq Station combo: " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: " + str(total_travel_time))

    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("User types: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("Gender Count : \n" + str(gender))
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth : {}\n'.format(earliest_birth))
        print('Recent birth : {}\n'.format(most_recent_birth))
        print('Common birth : {}\n'.format(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nView next five (5) rows of data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nView first five (5) row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
