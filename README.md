<!-- Author (Created): Roger "Equah" Hürzeler -->
<!-- Date (Created): 12019.12.25 HE -->
<!-- License: apache-2.0 -->

**Historia [Python 3]**
================================================================================

[Historia](https://github.com/TheEquah/Historia/) Python 3 implementation.

--------------------------------------------------------------------------------

# Architecture

Overview of the Historia architecture.

## Log

The log message object contains time, level, location, message and data of the log message.

### Time

The log message time is taken from `time.time()`.

### Location

The log message location defines where the message originates from in the format `my.package > Class.function(self, example) > n`.

### Message

The message defines a human readable text for this message.

## Log level

The log level defines the context of the message. Historia defines the following log levels:

| Sortcut | Name        | Constant                         | Description            |
| :------ | :---------- | :------------------------------- | :--------------------- |
| I       | Information | `equah.historia.Log.LVL_INFO`    | General information.   |
| W       | Warning     | `equah.historia.Log.LVL_WARNING` | General warning.       |
| E       | Error       | `equah.historia.Log.LVL_ERROR`   | Critical error.        |
| N       | Notice      | `equah.historia.Log.LVL_NOTE`    | Important information. |

## Log Data

Log message data is stored in a dictionary. The index defines the name of the value.

--------------------------------------------------------------------------------

# Install

Historia provedes a [`/src/setup.py`](https://github.com/TheEquah/Historia-python3/blob/master/src/setup.py) script to install the historia package. To use this script, `cd` into the [`src`](https://github.com/TheEquah/Historia-python3/tree/master/src/) directory, and execute the script with `python3 ./setup.py install`.

--------------------------------------------------------------------------------

# Examples

This repository provides the following example uses for Historia.

## Counter

A simple counter example script.

Directory: [`/example/counter/`](https://github.com/TheEquah/Historia-python3/tree/master/example/counter/)

--------------------------------------------------------------------------------
