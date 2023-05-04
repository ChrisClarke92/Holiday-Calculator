destination = 0    # Variables that will be added to later
nights = 0
car = 0

valid_choice = False   # This section takes the users choice and adjusts the destination variable
while valid_choice == False:
    print('You can fly to Barcelona, Rome or Lisbon')
    city_flight = (input('Please type which city you are flying to: ')).lower()
    if city_flight == 'barcelona':
        valid_choice = True
        destination = 200
    elif city_flight == 'rome':
        valid_choice = True
        destination = 175
    elif city_flight == 'lisbon':
        valid_choice = True
        destination = 150
    else:
        print('That is not a valid input')
         
while True:   # This section takes the number of nights the user wants and adjusts the nights variable
    try:
        num_nights = int(input('Type the number of nights you wish to stay: '))
        nights += num_nights
        break
    except:
        print('That is not a valid entry')

while True:   # This section takes the number of rental car days needed and adjusts the car variable
    try:
        rental_days = int(input('Type the number of days you require a rental car: '))
        car += rental_days
        break
    except:
        print('That is not a valid entry')
           
def hotel_cost(x, y=90):   # Function to work out the hotel cost using the nights variable multiplied by 90
    total_hotel = x * y
    return(total_hotel)
hotel_charge = hotel_cost(nights)

def car_rental(x, y=50):   # Function to work out the rental car charge using the car variable mulitplied by 50
    total_car = x * y
    return(total_car)
car_charge = car_rental(car)

def holiday_cost(x, y, z):   # Function that totals the three charges - destination, hotel_charge and car_charge 
    total_holiday = x + y + z
    return(total_holiday)
holiday_charge = holiday_cost(destination, hotel_charge, car_charge)

print(f'\nYour holiday will cost you a total of €{holiday_charge}\n')   # Total of the holiday plus the breakdown of each charge
print('A BREAKDOWN OF YOUR CHARGES:\n')
print(f'Flights - €{destination}')
print(f'Hotel - €{hotel_charge}')
print(f'Car Rental - €{car_charge}')