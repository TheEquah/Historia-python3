# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12019.12.25 HE
# License: apache-2.0


import time


# [>] Log
# [i] Log message object.
class Log :
    
    # [i] Log message levels.
    LVL_NONE = ("0", "None")
    LVL_INFO = ("I", "Information")
    LVL_WARNING = ("W", "Warning")
    LVL_ERROR = ("E", "Error")
    LVL_NOTE = ("N", "Notice")
    
    # [>] Initialize
    def __init__(self) :
        
        # [>] Time
        # [i] Stores the time when this message was created.
        self.time = 0
        
        # [>] Level
        # [i] Context of this message.
        self.level = Log.LVL_NONE
        
        # [>] Location
        # [i] Log message origin.
        self.location = ""
        
        # [>] Message
        # [i] Text information of this message.
        self.message = ""
        
        # [>] Data
        # [i] Dictionary of message data.
        self.data = {}
        
        return
    
    # [>] Compose
    # [i] Compose this log message to a string.
    # [R] {str} => String of composed log message.
    def compose(self) :
        
        # [i] Format base message.
        msg_str = "\n[{}] {} | {} | {}\n".format(
            self.level[1],
            self.time,
            self.location,
            self.message
        )
        
        # [i] Format message data.
        for data_name in self.data :
            msg_str += "\t{}: {};\n".format(
                data_name,
                self.data[data_name]
            )
            pass
        
        return msg_str


# [>] Log
# [i] Write a log message.
# [P] {tuple} lvl (Log.LVL_NONE) => Levelof this log message from `Log.LVL_*`.
# [P] {str} loc ("") => Location of this log message.
# [P] {str} msg ("") => Message of this log message.
# [P] {dict} data ({}) => Dictionary containing data related to this message, where index is the name.
def log(lvl=Log.LVL_NONE, loc="", msg="", data={}) :
    
    log_time = time.time()
    
    # [i] Build log message.
    log_msg = Log()
    log_msg.time = log_time
    log_msg.level = lvl
    log_msg.location = loc
    log_msg.message = msg
    log_msg.data = data
    
    OUTPUT_FN(log_msg)
    
    return log_msg

# [>] Output Print
# [i] Output the log message with print.
# [P] {Log} log_msg => Log message to print.
def output_print(log_msg) :
    
    print(log_msg.compose(), end="")
    
    return

# [>] Output Function
# [i] Default function to output log message object.
OUTPUT_FN = output_print
