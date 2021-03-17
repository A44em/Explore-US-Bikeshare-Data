import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = input("\nPlease enter the name of the city like this: Chicago, New York City or Washington):\n ").lower().strip()

    while city not in cities:
        city = input("\nPlease enter the name of the city correctly:\n ").lower().strip()

    # get user input for month (all, january, february, ... , june)
    months = ["all", "jan", "feb", "mar", "apr", "may", "jun"]
    month = input("\nPlease enter the month like this: JAN, FEB, MAR, APR, MAY, JUN or all:\n ").lower().strip()

    while month not in months:
        month = input("\nPlease enter the month correctly:\n ").lower().strip()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    week = ["all", "mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    day = input("\nPlease enter the day like this: Mon, Tue, Wed, Thu, Fri, Sat, Sun or all:\n ").lower().strip()

    while day not in week:
        day = input("\nPlease enter the day correctly:\n ").lower().strip()

    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the corresponding int
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        day = days.index(day) + 1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mcom_month = df['month'].mode()[0]
    print("Most common month: ", mcom_month)

    # display the most common day of week
    mcom_day = df['day_of_week'].mode()[0]
    print("Most common day: ", mcom_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mcom_hour = df['hour'].mode()[0]
    print("Most common hour: ", mcom_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mcom_start_station = df['Start Station'].mode()[0]
    print("Most common start station: ", mcom_start_station)

    # display most commonly used end station
    mcom_end_station = df['End Station'].mode()[0]
    print("Most common end station: ", mcom_end_station)

    # display most frequent combination of start station and end station trip
    mcom_combination_stations = df['Start Station'] + df['End Station']
    print("Most common combination of stations: ", mcom_combination_stations.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # display total travel time
    df['Travel Time'] = df['End Time'].dt.hour - df['Start Time'].dt.hour
    total_travel_time = df['Travel Time'].sum()
    print("Total Travel Time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print("Mean Travel Time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    print(gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    recent_year = df['Birth Year'].max()
    mcom_year = df['Birth Year'].mode()[0]
    print("Earliest year: ", earliest_year)
    print("Most recent year: ", recent_year)
    print("Most common year: ", mcom_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
