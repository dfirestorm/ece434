# hw06
## Preempt RT kernel
this homework consists mostly of a youtube video on RT kernels and compiling and running one of such kernels
### project
I added a project about using a microphone to create a audio spectrum display with the beagle. 
### watch
watching the video, my answers to the questions are as follows: 
    1. Where does Julia Cartwright work?
        National Instruments
    2. What is PREEMPT_RT? Hint: Google it.
        a patch for the linux kernel that can allow it to run in full realtime
    3. What is mixed criticality?
        running both real-time and non-time critical tasks on the same system and having them interact
    4. How can drivers misbehave?
        the rt and non rt drivers share stacks so the drivers can misbehave
    5. What is Δ in Figure 1?
        the delta - the time between the interrupt occuring and the relevant RT task executing
    6. What is Cyclictest[2]?
        a test that takes a timestamp, sleeps for a fixed duration, and then takes another timestamp and compares the difference to find the delta
    7. What is plotted in Figure 2?
        a histogram that plots the preempt rt and regular preempt performance in cyclictest
    8. What is dispatch latency? Scheduling latency?
        the dispatch latency is the time between hardware firing and the interrupt triggering the task in software. the scheduling latency is the time between the task trigger and the CPU starting the task
    9. What is mainline?
        mainline is the main linux kernel context, or the non-rt kernel components
    10. What is keeping the External event in Figure 3 from starting?
        another interrupt from non rt linux which inherently runs while ignoring interrupts
    11. Why can the External event in Figure 4 start sooner?
        the RT kernel runs shims in the irq disabled context to start the other tasks in threads, allowing other more important tasks to be started and run on top of less important irqs
### preempt rt
 kernel installed, tests run and placed in rt subfolder. one has a 400 max due to having to recopy the hist.gen but not fixing it again. 