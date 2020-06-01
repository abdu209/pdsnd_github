import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all' ]

def get_filters(city, month, day):

    # 
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city not in cities:
            print("\nInvalid Answer\n")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('All right! n\ Which month would you like analyze? January, Feburary, March, April, May, June, All?\n').lower()
        if month not in months:
            print("\nInvalid Answer\n")
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day or days of the week would you like to analyze?\n').lower()
        if day not in days:
            print("\nInvalid Answer\n")
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_popular_month = df['month'].mode()[0]
    print(most_popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_popular_dow = df['day_of_week'].mode()[0]
    print(most_popular_dow)


    # TO DO: display the most common start hour
    df['start_time'] = pd.to_datetime(df['Start Time'])
    most_popular_hour = df['start_time'].mode()[0]
    print(most_popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
 
    print('Most Common Start Station:', popular_start)
    print('')
 
    # TO DO: display most commonly used end station

    popular_end = df['End Station'].mode()[0]
 
    print('Most Common End Station:', popular_end)
    print('')
 
    # TO DO: display most frequent combination of start station and end station trip

    df['combo'] = df['Start Station'] + ' to ' + df['End Station']
    popular_station = df['combo'].mode()[0]
 
    print('Popular Combination:', popular_station)
    print('')
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts() 
    print(user_types)

   
    # TO DO: Display counts of gender
   
    if 'Gender' in df:
        count_of_gender = df['Gender'].value_counts()
        print('the count of gender is: ', count_of_gender)
    else:
        print("there is no gender data")
    

# TO DO: Display earliest, most recent, and most common year of birth
  
    print('\nDisplaying date of birth Stats...\n')   

    earliest_YOB = df['Birth Year'].min()
    print('earliest date of birth is ',earliest_YOB)
    
    most_recent_YOB = df['Birth Year'].max()
    print('most recent date of birth is ',most_recent_YOB)
    
    most_common_YOB = df['Birth Year'].mode()[0]
    print('most common date of birth is ',most_common_YOB)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    city = ""
    month = 0
    day = 0
    while True:
        city, month, day = get_filters(city, month, day)
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

