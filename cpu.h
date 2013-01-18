#ifndef CPU_H_INCLUDE 
#define CPU_H_INCLUDE 

struct proc_cpu_t {  
    int user_processes; // User processes in execution
    int niced;          // niced processes in user mode
    int system;         // processes executing in kernel mode
    int idle;           // Idle time
    int irq;            // Interrupt services
    int softirq;        // Servicing softirqs
}

#endif
