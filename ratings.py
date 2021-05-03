"""Restaurant rating lister."""

def rate_restaurant(restaurant_scores):

    scores_file = open(restaurant_scores)
    

    restaurant_rating = {}
    sorted_restaurants = []
    for restaurant in scores_file:
        restaurant = restaurant.rstrip()
        restaurant = restaurant.split(":")
        sorted_restaurants.append(restaurant)
    
    sorted_restaurants = sorted(sorted_restaurants)
    for restaurant in sorted_restaurants:
        restaurant_rating[restaurant[0]] = restaurant[1]
        print(f"{restaurant[0]} is rated at {restaurant[1]}.")



rate_restaurant("scores.txt")