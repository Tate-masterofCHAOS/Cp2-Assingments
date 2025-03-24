# Tate Morgan, Degubbing Notes
import trace
import sys

def trace_calls(frame, event, arg):
    if event == 'call': #When the function is called
        print(f"Calling function: {frame.f_code.co_name}")
    elif event == 'line': #When a new line of code appears
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return': #When we return stuff
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception': #Triggered when there is an exception
        print(f'Exception in {frame.f_code.co_name}: {arg}')

    return trace_calls

sys.settrace(trace_calls)
tracer = trace.Trace(count=False, trace=True)
#What is tracing?
    #Access information about the functions in your program
def add(numone, numtwo):
    print(sub(numone, numtwo))
    return numone + numtwo

def sub(numone, numtwo): 
    return numone - numtwo

print(add(5,2))

#tracer.run('add(8,9)')
    #Basic Tracing Command
        #python -m trace --trace Notes\tracing.py
'''
    --trace (displays lines as executed)
    --count (displays number of times executed)
    --listfunc (displays functoins used in program)
    --trackcalls (displays relationshipis between functions)
'''
#What are some ways we can debug by tracing?
    #Use the path to figure out where the bugs are occurring

#How do you access the debugger in VS Code?
    #Press debug button on the left or F5 or ctrl shift e or use the drop down by the play button

#What is testing?
    #Running your code to make sure it works as required, trying to break it

#What are boundary conditions?
    #A boundary condition is testing the condition most likely to be wrong

#How do you handle when users give strange inputs?
    #Basic conditions and loops
