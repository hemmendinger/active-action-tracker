active-action-tracker
=====================

For tracking wtf you were doing and wth else you need to do next via the cli 
when in a project without breaking context, ADD-friendly.

Problem addressed/goal of project: 
    Adding or referencing a to-do list while working can be distracting, resulting
    in frequent tangents. Which is harmful to any happy programmer's focus and flow.

    This program will allow a programmer to add and signal completion of tasks. 
    Ideally, a task is broken down into independent action-able items, or actions,
    in the spirit of the 'GTD' system, and only a signal action from a queue of 
    actions being worked on until completion.

-a, --action
    Display current action.

-n 'NEW ACTION', --new 'NEW ACTION'
    Add new action as a quoted string.

-d 1, --delete 1
    Delete current action.

-c 1, --cycle 1
    Cycle to the next action.

-r 1, --r 1
    Reverse the queue.
