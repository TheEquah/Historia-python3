# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12019.12.25 HE
# License: apache-2.0

import equah.historia

# [i] Local variables.
counter = 0
counter_name = "Example counter"

# [>] Counter Increment
# [i] Increments the counter value by given value.
# [P] {int} inc => Amount to add to the counter value.
def counter_increment(inc) :
    global counter
    
    counter += inc
    
    # [i] First log message in script.
    # [NOTE] Increment data uses special formatting.
    equah.historia.log(equah.historia.Log.LVL_INFO, "counter > counter_increment(inc) > 1", "Counter increment.", {
        "Counter before increment": counter-inc,
        "Counter increment": ">> {} <<".format(inc),
        "Counter after increment": counter
    })
    
    return

# [>] Counter Set
# [i] Sets the counter to a given value.
# [P] {int} set => Value to set the counter to.
def counter_set(set) :
    global counter
    
    previous_value = counter
    counter = set
    
    # [i] First log message in script.
    equah.historia.log(equah.historia.Log.LVL_INFO, "counter > counter_set(set) > 1", "Counter set.", {
        "Counter before set": previous_value,
        "Counter set value": counter
    })
    
    return

# [>] Main
if __name__ == "__main__":
    
    # [i] First log message in script.
    equah.historia.log(equah.historia.Log.LVL_INFO, "counter > __main__ > 1", "Counter example started.", {
        "Counter start value": counter,
        "Counter name": counter_name
    })
    
    # [i] Change counter value.
    counter_set(10)
    counter_increment(500)
    counter_increment(-120)
    counter_increment(30)
    
    # [i] Last log message in script.
    equah.historia.log(equah.historia.Log.LVL_INFO, "counter > __main__ > 2", "Counter example end.", {
        "Counter exit value": counter
    })
    
    exit()
