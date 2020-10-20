import copy

class WeightBreakdown:

    def __init__(self, press, deadlift, bench, squat):
        self.maxes = {'press' : press, 'deadlift' : deadlift, 'bench' : bench, 'squat' : squat}
    
    # Calculate a specific weight for a set on a specific day and round down to increment of 5 
    def calculate_set_weight(self, training_max, set_percentage):
        set_weight = float(training_max) * set_percentage
        return int(set_weight - (set_weight % 5))

    # Create a nested dictionary containing a set of working weights for each set that can be
    # easily converted to JSON for use in the html templates
    def build_workout(self):

        # Set percentages by week
        weeks = { 'week1' : [0.65, 0.75, 0.85], 'week2' : [0.7, 0.8, 0.9], 'week3' : [0.75, 0.85, 0.95], 'warmup_deload' : [0.4, 0.5, 0.6] }

        # Build four week cycle for each lift, each week, and each set 
        workout = {}
        lifts = ['press', 'deadlift', 'bench', 'squat']
        for lift in lifts:
            workout[lift] = {}
            for week, set_weights in weeks.items():
                week_copy = copy.deepcopy(week)
                workout[lift][week_copy]= []
                for set in set_weights:
                    set_copy = copy.deepcopy(set)
                    workout[lift][week_copy].append(self.calculate_set_weight( self.maxes[lift], set_copy ))
        return workout
